"""
generator.py — Sends parsed code metadata to IBM Bob and returns generated docs.

IBM Bob API is accessed via the 'bob' Python SDK (installed with IBM Bob VS Code extension).
Docs: https://ibm.github.io/bob-sdk

If running outside VS Code / IBM Bob environment, set the BOB_API_KEY env variable.
"""

import os
import json
from typing import List, Dict, Any
from .parser import ModuleInfo, FunctionInfo, ClassInfo


# ─── IBM Bob client setup ────────────────────────────────────────────────────

def _get_bob_client():
    """
    Initialise the IBM Bob client.
    Tries: 1) bob SDK (VS Code extension), 2) BOB_API_KEY env var, 3) mock for testing.
    """
    try:
        from bob import BobClient
        return BobClient()
    except ImportError:
        pass

    api_key = os.getenv("BOB_API_KEY")
    if api_key:
        try:
            from bob import BobClient
            return BobClient(api_key=api_key)
        except ImportError:
            pass

    print("  [Warning] IBM Bob SDK not found. Using mock generator for testing.")
    print("  Set BOB_API_KEY env var or run inside IBM Bob VS Code extension.")
    return None


# ─── Prompt builder ──────────────────────────────────────────────────────────

def _build_function_prompt(fn: FunctionInfo, module_name: str) -> str:
    sig_parts = []
    for arg in fn.args:
        part = arg.name
        if arg.annotation:
            part += f": {arg.annotation}"
        if arg.default:
            part += f" = {arg.default}"
        sig_parts.append(part)
    signature = f"{'async ' if fn.is_async else ''}def {fn.name}({', '.join(sig_parts)})"
    if fn.return_annotation:
        signature += f" -> {fn.return_annotation}"

    existing = f"\nExisting docstring:\n{fn.existing_docstring}" if fn.existing_docstring else ""

    return f"""You are a Python documentation expert. Generate a clear, complete Google-style docstring for this function.

Module: {module_name}
Function signature: {signature}{existing}

Return ONLY the docstring content (without the triple quotes), including:
- One-line summary
- Args section (with types and descriptions)
- Returns section
- Raises section (if applicable)
- A short usage example in an Example section
"""


def _build_class_prompt(cls: ClassInfo, module_name: str) -> str:
    bases = f"({', '.join(cls.bases)})" if cls.bases else ""
    method_names = [m.name for m in cls.methods if not m.name.startswith("__")]
    existing = f"\nExisting docstring:\n{cls.existing_docstring}" if cls.existing_docstring else ""

    return f"""You are a Python documentation expert. Generate a clear Google-style docstring for this class.

Module: {module_name}
Class: class {cls.name}{bases}{existing}
Public methods: {', '.join(method_names) if method_names else 'none'}

Return ONLY the docstring content (without triple quotes), including:
- One-line summary of what the class does
- Attributes section (if inferable)
- A short usage example
"""


def _build_module_prompt(mod: ModuleInfo) -> str:
    fn_names = [f.name for f in mod.functions]
    cls_names = [c.name for c in mod.classes]
    existing = f"\nExisting module docstring:\n{mod.existing_docstring}" if mod.existing_docstring else ""

    return f"""You are a Python documentation expert. Generate a module-level docstring.

Module: {mod.module_name}
File: {os.path.basename(mod.file_path)}{existing}
Top-level functions: {', '.join(fn_names) if fn_names else 'none'}
Classes: {', '.join(cls_names) if cls_names else 'none'}
Key imports: {', '.join(mod.imports[:5]) if mod.imports else 'none'}

Return ONLY the docstring content (no triple quotes): a 2-4 sentence description of the module's purpose.
"""


# ─── IBM Bob call ────────────────────────────────────────────────────────────

def _ask_bob(client, prompt: str, verbose: bool = False) -> str:
    """Send a prompt to IBM Bob and return the text response."""
    if client is None:
        return _mock_response(prompt)

    try:
        response = client.chat(
            messages=[{"role": "user", "content": prompt}],
            context="codebase",      # tells Bob to use repo context
            max_tokens=512,
        )
        return response.content.strip()
    except Exception as e:
        if verbose:
            print(f"  [Bob error] {e}")
        return _mock_response(prompt)


def _mock_response(prompt: str) -> str:
    """Fallback mock response for testing without IBM Bob."""
    if "Function signature:" in prompt or "def " in prompt:
        return (
            "Performs the specified operation.\n\n"
            "Args:\n    *args: Positional arguments.\n    **kwargs: Keyword arguments.\n\n"
            "Returns:\n    Result of the operation.\n\n"
            "Example:\n    >>> result = function()\n"
        )
    if "class " in prompt:
        return (
            "Represents the described entity.\n\n"
            "Attributes:\n    Attributes are set during initialisation.\n\n"
            "Example:\n    >>> obj = ClassName()\n"
        )
    return "Module providing core functionality for the project."


# ─── Main generator ──────────────────────────────────────────────────────────

@dataclass_like := lambda **kw: type("Docs", (), kw)  # lightweight namespace

def generate_docs(modules: List[ModuleInfo], project_name: str = "Project", verbose: bool = False) -> Dict[str, Any]:
    """
    For each module, generate AI docs for the module, its classes, and functions.
    Returns a dict keyed by module name with all generated documentation.
    """
    client = _get_bob_client()
    result = {
        "project": project_name,
        "modules": []
    }

    for mod in modules:
        if verbose:
            print(f"  Generating docs for: {mod.module_name}")

        mod_doc = {
            "name": mod.module_name,
            "file": mod.file_path,
            "docstring": _ask_bob(client, _build_module_prompt(mod), verbose),
            "functions": [],
            "classes": [],
        }

        for fn in mod.functions:
            doc = _ask_bob(client, _build_function_prompt(fn, mod.module_name), verbose)
            mod_doc["functions"].append({
                "name": fn.name,
                "is_async": fn.is_async,
                "args": [{"name": a.name, "annotation": a.annotation, "default": a.default} for a in fn.args],
                "return_annotation": fn.return_annotation,
                "decorators": fn.decorators,
                "docstring": doc,
            })

        for cls in mod.classes:
            cls_doc = {
                "name": cls.name,
                "bases": cls.bases,
                "docstring": _ask_bob(client, _build_class_prompt(cls, mod.module_name), verbose),
                "methods": [],
            }
            for method in cls.methods:
                doc = _ask_bob(client, _build_function_prompt(method, f"{mod.module_name}.{cls.name}"), verbose)
                cls_doc["methods"].append({
                    "name": method.name,
                    "is_async": method.is_async,
                    "args": [{"name": a.name, "annotation": a.annotation, "default": a.default} for a in method.args],
                    "return_annotation": method.return_annotation,
                    "docstring": doc,
                })
            mod_doc["classes"].append(cls_doc)

        result["modules"].append(mod_doc)

    return result
