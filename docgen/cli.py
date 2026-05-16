"""
CLI interface for DocGen.
Usage:
    python main.py ./my_project
    python main.py ./my_project --output ./docs --format html
    python main.py ./my_project --format all
"""

import click
import os
import sys
from .parser import parse_project
from .generator import generate_docs
from .exporter import export_markdown, export_html, export_pdf


@click.command()
@click.argument("source_path", type=click.Path(exists=True))
@click.option("--output", "-o", default="./output", help="Output directory for docs")
@click.option(
    "--format", "-f",
    type=click.Choice(["markdown", "html", "pdf", "all"], case_sensitive=False),
    default="markdown",
    help="Output format (default: markdown)"
)
@click.option("--project-name", "-n", default=None, help="Project name (auto-detected if omitted)")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed output")
def run(source_path, output, format, project_name, verbose):
    """DocGen: Generate docs for a Python project using IBM Bob AI."""

    project_name = project_name or os.path.basename(os.path.abspath(source_path))
    os.makedirs(output, exist_ok=True)

    click.echo(f"\n DocGen — IBM Bob Hackathon\n")
    click.echo(f" Project : {project_name}")
    click.echo(f" Source  : {os.path.abspath(source_path)}")
    click.echo(f" Output  : {os.path.abspath(output)}")
    click.echo(f" Format  : {format}\n")

    # Step 1: Parse
    click.echo("Step 1/3  Parsing Python source...")
    modules = parse_project(source_path, verbose=verbose)
    click.echo(f"          Found {len(modules)} module(s)\n")

    if not modules:
        click.echo("No Python files found. Exiting.", err=True)
        sys.exit(1)

    # Step 2: Generate with IBM Bob
    click.echo("Step 2/3  Sending to IBM Bob for documentation...")
    docs = generate_docs(modules, project_name=project_name, verbose=verbose)
    click.echo("          Documentation generated\n")

    # Step 3: Export
    click.echo("Step 3/3  Exporting...")

    if format in ("markdown", "all"):
        path = export_markdown(docs, output, project_name)
        click.echo(f"          Markdown  → {path}")

    if format in ("html", "all"):
        path = export_html(docs, output, project_name)
        click.echo(f"          HTML      → {path}")

    if format in ("pdf", "all"):
        path = export_pdf(docs, output, project_name)
        click.echo(f"          PDF       → {path}")

    click.echo(f"\n Done! Docs saved to: {os.path.abspath(output)}\n")
