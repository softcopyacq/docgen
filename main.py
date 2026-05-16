import sys
import os
import streamlit as st
from docgen.cli import run

# 1. Set up a clean web layout
st.set_page_config(page_title="DocGen Dashboard", page_icon="📄", layout="centered")

st.title("📄 AI Documentation Generator")
st.write("Welcome to the DocGen deployment interface. Click the button below to parse your project and generate markdown documentation.")

# 2. Add an interactive execution button
if st.button("🚀 Generate Documentation Now", type="primary"):
    with st.spinner("Parsing source files and building documentation..."):
        try:
            # Fallback for missing arguments in a web worker context
            if len(sys.argv) < 2:
                sys.argv.append(".")
            
            # Execute your documentation engine
            run()
            
            st.success("✨ Documentation generated successfully!")
            
            # 3. Read the output file so users can see/download it on the web page
            output_path = "./output/docgen_docs.md"
            if os.path.exists(output_path):
                with open(output_path, "r", encoding="utf-8") as f:
                    markdown_content = f.read()
                
                st.subheader("Preview Generated Docs:")
                st.text_area("Markdown Output", value=markdown_content, height=300)
                
                st.download_button(
                    label="📥 Download docgen_docs.md",
                    data=markdown_content,
                    file_name="docgen_docs.md",
                    mime="text/markdown"
                )
            else:
                st.warning("Documentation completed, but output file was not found in the default path.")
                
        except Exception as e:
            st.error(f"An execution error occurred: {e}")
