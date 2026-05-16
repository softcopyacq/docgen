# DocGen — AI-Powered Docs Generator

> IBM Bob Hackathon 2026 · "Your repo. Your rules. AI as your dev partner."

DocGen uses **IBM Bob** to automatically generate rich, accurate documentation for any Python codebase — from docstrings to a full HTML site.

---

## Quickstart

```bash
# 1. Install dependencies
pip install click

# 2. Run on your project
python main.py ./your_project

# 3. Get all formats
python main.py ./your_project --format all --output ./docs
```

## How it works

1. **AST Parser** — scans your Python files using `ast` + `inspect`, extracting functions, classes, type hints, and existing docstrings
2. **IBM Bob** — receives the structured metadata and generates Google-style docstrings with usage examples
3. **Exporter** — renders the docs as Markdown, HTML, or PDF

## CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `source_path` | Path to your Python project or file | required |
| `--output` | Output directory | `./output` |
| `--format` | `markdown`, `html`, `pdf`, or `all` | `markdown` |
| `--project-name` | Project name in docs | auto-detected |
| `--verbose` | Show detailed progress | off |

## IBM Bob Integration

Set your IBM Bob API key:
```bash
export BOB_API_KEY=your_key_here
```
Or run directly inside the IBM Bob VS Code extension — it auto-detects the client.

## GitHub Action

Add `.github/workflows/docs.yml` to auto-regenerate docs on every push.
Add `BOB_API_KEY` to your repo secrets.

## Output

- `*_docs.md` — Markdown API reference
- `*_docs.html` — Browsable HTML docs site
- `*_docs.pdf` — PDF report (requires `weasyprint`)

---

Built for the IBM Bob Hackathon 2026 · lablab.ai
