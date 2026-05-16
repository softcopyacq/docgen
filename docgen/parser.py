"""
parser.py — Extracts structured metadata from Python source files using AST.
Collects: modules, classes, functions, type hints, existing docstrings.
"""

import ast
import os
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ArgInfo:
    name: str
    annotation: Optional[str] = None
    default: Optional[str] = None


@dataclass
class FunctionInfo:
    name: str
    args: List[ArgInfo] = field(default_factory=list)
    return_annotation: Optional[str] = None
    existing_docstring: Optional[str] = None
    decorators: List[str] = field(default_factory=list)
    is_async: bool = False
    lineno: int = 0


@dataclass
class ClassInfo:
    name: str
    methods: List[FunctionInfo] = field(default_factory=list)
    bases: List[str] = field(default_factory=list)
    existing_docstring: Optional[str] = None
    lineno: int = 0


@dataclass
class ModuleInfo:
    file_path: str
    module_name: str
    functions: List[FunctionInfo] = field(default_factory=list)
    classes: List[ClassInfo] = field(default_factory=list)
    existing_docstring: Optional[str] = None
    imports: List[str] = field(default_factory=list)


def _annotation_to_str(node) -> Optional[str]:
    """Convert an AST annotation node to a string."""
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return str(node)


def _parse_function(node: ast.FunctionDef | ast.AsyncFunctionDef) -> FunctionInfo:
    args = []
    all_args = node.args

    # Collect defaults aligned to args
    num_defaults = len(all_args.defaults)
    num_args = len(all_args.args)
    defaults_pad = [None] * (num_args - num_defaults) + list(all_args.defaults)

    for i, arg in enumerate(all_args.args):
        if arg.arg == "self":
            continue
        default_node = defaults_pad[i]
        default_str = None
        if default_node:
            try:
                default_str = ast.unparse(default_node)
            except Exception:
                default_str = "..."
        args.append(ArgInfo(
            name=arg.arg,
            annotation=_annotation_to_str(arg.annotation),
            default=default_str,
        ))

    docstring = ast.get_docstring(node)
    decorators = [ast.unparse(d) for d in node.decorator_list]

    return FunctionInfo(
        name=node.name,
        args=args,
        return_annotation=_annotation_to_str(node.returns),
        existing_docstring=docstring,
        decorators=decorators,
        is_async=isinstance(node, ast.AsyncFunctionDef),
        lineno=node.lineno,
    )


def _parse_class(node: ast.ClassDef) -> ClassInfo:
    methods = []
    for item in node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            methods.append(_parse_function(item))

    bases = [ast.unparse(b) for b in node.bases]
    docstring = ast.get_docstring(node)

    return ClassInfo(
        name=node.name,
        methods=methods,
        bases=bases,
        existing_docstring=docstring,
        lineno=node.lineno,
    )


def parse_file(file_path: str) -> Optional[ModuleInfo]:
    """Parse a single Python file and return its ModuleInfo."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=file_path)
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"  Warning: Could not parse {file_path}: {e}")
        return None

    module_name = os.path.splitext(os.path.basename(file_path))[0]
    docstring = ast.get_docstring(tree)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            try:
                imports.append(ast.unparse(node))
            except Exception:
                pass

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(_parse_function(node))
        elif isinstance(node, ast.ClassDef):
            classes.append(_parse_class(node))

    return ModuleInfo(
        file_path=file_path,
        module_name=module_name,
        functions=functions,
        classes=classes,
        existing_docstring=docstring,
        imports=imports,
    )


def parse_project(source_path: str, verbose: bool = False) -> List[ModuleInfo]:
    """Recursively parse all Python files in a directory."""
    modules = []

    if os.path.isfile(source_path) and source_path.endswith(".py"):
        m = parse_file(source_path)
        if m:
            modules.append(m)
        return modules

    for root, dirs, files in os.walk(source_path):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__pycache__", "venv", ".venv", "node_modules"))]
        for filename in sorted(files):
            if filename.endswith(".py") and not filename.startswith("."):
                path = os.path.join(root, filename)
                if verbose:
                    print(f"  Parsing: {path}")
                m = parse_file(path)
                if m:
                    modules.append(m)

    return modules
