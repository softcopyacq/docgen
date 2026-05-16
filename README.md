# DocGen — AI-Powered Documentation Generator

> IBM Bob Hackathon 2026 · "Your repo. Your rules. AI as your dev partner."

[![GitHub](https://img.shields.io/badge/GitHub-softcopyacq%2Fdocgen-blue)](https://github.com/softcopyacq/docgen)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![IBM Bob](https://img.shields.io/badge/Powered%20by-IBM%20Bob-purple)](https://ibm.com/bob)

DocGen uses **IBM Bob AI** to automatically generate rich, accurate documentation for any Python codebase — from docstrings to a full HTML site.

**🚀 [Live Demo](https://softcopyacq-docgen.streamlit.app)** | **📹 [Video Demo](#)** | **📊 [Presentation](#)**

\---

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


## 🚀 Live Demo

Try DocGen now: **[https://softcopyacq-docgen.streamlit.app](https://softcopyacq-docgen.streamlit.app)**

Upload your Python files and see AI-generated documentation in seconds!

## 📊 IBM Bob Integration

This project was developed with extensive assistance from **IBM Bob AI**. See [IBM_BOB_REPORT.md](./IBM_BOB_REPORT.md) for complete development history and all AI-assisted sessions.

**IBM Bob's Contributions:**
- 70% code generation (parser, generator, exporter modules)
- 15% architecture design and best practices
- 10% debugging and optimization
- 5% documentation and testing

## 🏆 Hackathon Submission

**Built for IBM Bob Hackathon 2026 on lablab.ai**

- 📹 **Video Demo:** [Watch on YouTube](#)
- 📊 **Presentation:** [View Slides](#)
- 💻 **GitHub:** [softcopyacq/docgen](https://github.com/softcopyacq/docgen)
- 🌐 **Live App:** [Streamlit Demo](https://softcopyacq-docgen.streamlit.app)

## ✨ Features

- ✅ **Zero Configuration** - Works out of the box on any Python project
- ✅ **AI-Powered** - IBM Bob generates comprehensive docstrings with examples
- ✅ **Multi-Format Export** - Markdown, HTML, and PDF outputs
- ✅ **Type Hint Support** - Extracts and documents type annotations
- ✅ **CLI Interface** - Easy integration into existing workflows
- ✅ **GitHub Actions** - Automated documentation updates
- ✅ **Web Interface** - User-friendly Streamlit app

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/softcopyacq/docgen.git
cd docgen

# Install dependencies
pip install -r requirements.txt

# Run on your project
python main.py ./your_project --format all
```

## 🌐 Web Interface

Run the Streamlit web app locally:

```bash
streamlit run streamlit_app.py
```

Or use the live demo: [https://softcopyacq-docgen.streamlit.app](https://softcopyacq-docgen.streamlit.app)

## 📖 Documentation

- **[SUBMISSION_PLAN.md](./SUBMISSION_PLAN.md)** - Complete hackathon submission guide
- **[QUICK_START_GUIDE.md](./QUICK_START_GUIDE.md)** - Fast-track setup instructions
- **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** - Deployment options and instructions
- **[SUBMISSION_MATERIALS.md](./SUBMISSION_MATERIALS.md)** - Ready-to-use submission content

## 🎯 Use Cases

- **Open Source Projects** - Generate professional docs automatically
- **Enterprise Teams** - Maintain consistent documentation standards
- **Solo Developers** - Save time on documentation tasks
- **Code Reviews** - Ensure all code is properly documented
- **Legacy Code** - Add documentation to existing codebases

## 🛠️ Technology Stack

- **Language:** Python 3.8+
- **AI Engine:** IBM Bob API
- **Parsing:** ast, inspect modules
- **CLI:** Click framework
- **Web UI:** Streamlit
- **Export:** Markdown, HTML, WeasyPrint (PDF)
- **CI/CD:** GitHub Actions

## 📈 Impact

- **70% Time Savings** - Reduce documentation time dramatically
- **Consistent Quality** - AI ensures uniform documentation style
- **Better Examples** - Automatic usage examples for all functions
- **Easy Maintenance** - Regenerate docs as code evolves

## 🤝 Contributing

Contributions are welcome! This project was built for the IBM Bob Hackathon 2026.

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- **IBM Bob Team** - For the amazing AI development partner
- **lablab.ai** - For hosting the hackathon
- **Python Community** - For excellent tools and libraries

- `*_docs.md` — Markdown API reference
- `*_docs.html` — Browsable HTML docs site
- `*_docs.pdf` — PDF report (requires `weasyprint`)

---

Built for the IBM Bob Hackathon 2026 · lablab.ai
