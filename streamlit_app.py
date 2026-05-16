"""
Streamlit web interface for DocGen - AI Documentation Generator
Deploy this to Streamlit Cloud for the hackathon demo
"""

import streamlit as st
import tempfile
import os
import sys
from pathlib import Path

# Add docgen to path
sys.path.insert(0, str(Path(__file__).parent))

from docgen.parser import parse_project
from docgen.generator import generate_docs
from docgen.exporter import export_markdown, export_html

# Page config
st.set_page_config(
    page_title="DocGen - AI Documentation Generator",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 DocGen - AI Documentation Generator")
st.markdown("**Powered by IBM Bob AI** | Built for IBM Bob Hackathon 2026")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("About DocGen")
    st.write("""
    DocGen automatically generates comprehensive documentation for Python projects using IBM Bob AI.
    
    **Features:**
    - 🔍 AST-based code parsing
    - 🤖 AI-generated docstrings
    - 📝 Multiple export formats
    - ✨ Usage examples included
    """)
    
    st.markdown("---")
    st.markdown("### How to Use")
    st.write("1. Upload Python files")
    st.write("2. Click 'Generate Documentation'")
    st.write("3. View results below")
    
    st.markdown("---")
    st.markdown("[GitHub](https://github.com/yourusername/docgen) | [Video Demo](#)")

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📤 Upload Python Files")
    uploaded_files = st.file_uploader(
        "Choose Python files (.py)",
        type="py",
        accept_multiple_files=True,
        help="Upload one or more Python files to generate documentation"
    )
    
    project_name = st.text_input(
        "Project Name",
        value="MyProject",
        help="Name for your documentation"
    )
    
    format_option = st.selectbox(
        "Output Format",
        ["HTML (Interactive)", "Markdown", "Both"],
        help="Choose documentation format"
    )

with col2:
    st.header("⚙️ Options")
    show_verbose = st.checkbox("Show detailed progress", value=False)

# Generate button
if st.button("🚀 Generate Documentation", type="primary", use_container_width=True):
    if not uploaded_files:
        st.error("Please upload at least one Python file!")
    else:
        with st.spinner("Generating documentation with IBM Bob AI..."):
            try:
                with tempfile.TemporaryDirectory() as tmpdir:
                    st.info(f"📁 Processing {len(uploaded_files)} file(s)...")
                    for file in uploaded_files:
                        file_path = os.path.join(tmpdir, file.name)
                        with open(file_path, "wb") as f:
                            f.write(file.getbuffer())
                    
                    st.info("🔍 Parsing Python code...")
                    modules = parse_project(tmpdir, verbose=show_verbose)
                    
                    if not modules:
                        st.error("No valid Python modules found in uploaded files.")
                    else:
                        st.success(f"✅ Found {len(modules)} module(s)")
                        
                        st.info("🤖 Generating documentation with IBM Bob AI...")
                        docs = generate_docs(modules, project_name=project_name, verbose=show_verbose)
                        
                        if format_option in ["HTML (Interactive)", "Both"]:
                            html_path = export_html(docs, tmpdir, project_name)
                            with open(html_path, "r", encoding="utf-8") as f:
                                html_content = f.read()
                        
                        if format_option in ["Markdown", "Both"]:
                            md_path = export_markdown(docs, tmpdir, project_name)
                            with open(md_path, "r", encoding="utf-8") as f:
                                md_content = f.read()
                        
                        st.success("✨ Documentation generated successfully!")
                        
                        st.markdown("---")
                        st.header("📄 Generated Documentation")
                        
                        if format_option == "HTML (Interactive)":
                            st.components.v1.html(html_content, height=800, scrolling=True)
                            st.download_button(
                                "⬇️ Download HTML",
                                html_content,
                                file_name=f"{project_name}_docs.html",
                                mime="text/html"
                            )
                        
                        elif format_option == "Markdown":
                            st.markdown(md_content)
                            st.download_button(
                                "⬇️ Download Markdown",
                                md_content,
                                file_name=f"{project_name}_docs.md",
                                mime="text/markdown"
                            )
                        
                        else:
                            tab1, tab2 = st.tabs(["HTML Preview", "Markdown"])
                            with tab1:
                                st.components.v1.html(html_content, height=800, scrolling=True)
                                st.download_button(
                                    "⬇️ Download HTML",
                                    html_content,
                                    file_name=f"{project_name}_docs.html",
                                    mime="text/html",
                                    key="html_download"
                                )
                            with tab2:
                                st.markdown(md_content)
                                st.download_button(
                                    "⬇️ Download Markdown",
                                    md_content,
                                    file_name=f"{project_name}_docs.md",
                                    mime="text/markdown",
                                    key="md_download"
                                )
            
            except Exception as e:
                st.error(f"❌ Error generating documentation: {str(e)}")
                if show_verbose:
                    st.exception(e)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Built with ❤️ for IBM Bob Hackathon 2026 | Powered by IBM Bob AI</p>
    <p>DocGen - Making documentation effortless</p>
</div>
""", unsafe_allow_html=True)

# Made with Bob
