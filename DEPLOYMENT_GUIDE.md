# DocGen - Deployment Guide

## 🚀 Deployment Options for Demo Application

### Option 1: Streamlit Cloud (Recommended - Easiest)

#### Step 1: Create Streamlit App

Create a file named `streamlit_app.py` in your project root with this content:

```python
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
    include_private = st.checkbox("Include private methods", value=False)

# Generate button
if st.button("🚀 Generate Documentation", type="primary", use_container_width=True):
    if not uploaded_files:
        st.error("Please upload at least one Python file!")
    else:
        with st.spinner("Generating documentation with IBM Bob AI..."):
            try:
                # Create temporary directory
                with tempfile.TemporaryDirectory() as tmpdir:
                    # Save uploaded files
                    st.info(f"📁 Processing {len(uploaded_files)} file(s)...")
                    for file in uploaded_files:
                        file_path = os.path.join(tmpdir, file.name)
                        with open(file_path, "wb") as f:
                            f.write(file.getbuffer())
                    
                    # Parse project
                    st.info("🔍 Parsing Python code...")
                    modules = parse_project(tmpdir, verbose=show_verbose)
                    
                    if not modules:
                        st.error("No valid Python modules found in uploaded files.")
                    else:
                        st.success(f"✅ Found {len(modules)} module(s)")
                        
                        # Generate docs
                        st.info("🤖 Generating documentation with IBM Bob AI...")
                        docs = generate_docs(modules, project_name=project_name, verbose=show_verbose)
                        
                        # Export based on format
                        if format_option in ["HTML (Interactive)", "Both"]:
                            html_path = export_html(docs, tmpdir, project_name)
                            with open(html_path, "r", encoding="utf-8") as f:
                                html_content = f.read()
                        
                        if format_option in ["Markdown", "Both"]:
                            md_path = export_markdown(docs, tmpdir, project_name)
                            with open(md_path, "r", encoding="utf-8") as f:
                                md_content = f.read()
                        
                        st.success("✨ Documentation generated successfully!")
                        
                        # Display results
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
                        
                        else:  # Both
                            tab1, tab2 = st.tabs(["HTML Preview", "Markdown"])
                            with tab1:
                                st.components.v1.html(html_content, height=800, scrolling=True)
                                st.download_button(
                                    "⬇️ Download HTML",
                                    html_content,
                                    file_name=f"{project_name}_docs.html",
                                    mime="text/html"
                                )
                            with tab2:
                                st.markdown(md_content)
                                st.download_button(
                                    "⬇️ Download Markdown",
                                    md_content,
                                    file_name=f"{project_name}_docs.md",
                                    mime="text/markdown"
                                )
            
            except Exception as e:
                st.error(f"❌ Error generating documentation: {str(e)}")
                if show_verbose:
                    st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Built with ❤️ for IBM Bob Hackathon 2026 | Powered by IBM Bob AI</p>
    <p>DocGen - Making documentation effortless</p>
</div>
""", unsafe_allow_html=True)
```

#### Step 2: Update requirements.txt

Add Streamlit to your `requirements.txt`:

```
click>=8.0
weasyprint>=60.0
streamlit>=1.28.0
```

#### Step 3: Deploy to Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git add streamlit_app.py requirements.txt
   git commit -m "Add Streamlit web interface"
   git push origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub account
   - Select your repository
   - Set main file: `streamlit_app.py`
   - Click "Deploy"

3. **Get your URL:**
   - Your app will be at: `https://yourusername-docgen-streamlit-app-xxxxx.streamlit.app`
   - Use this URL in your hackathon submission

---

### Option 2: Replit (Alternative)

#### Step 1: Import to Replit

1. Go to [replit.com](https://replit.com)
2. Click "Create Repl"
3. Select "Import from GitHub"
4. Enter your repository URL
5. Click "Import from GitHub"

#### Step 2: Configure Replit

Create `.replit` file in project root:

```toml
run = "python main.py ./sample_project --format all"
language = "python3"

[nix]
channel = "stable-22_11"

[deployment]
run = ["sh", "-c", "python main.py ./sample_project --format all"]
```

#### Step 3: Make Public & Share

1. Click "Share" button
2. Make Repl public
3. Copy the Repl URL
4. Use this URL in your submission

---

### Option 3: Vercel (For Web Interface)

If you create a web frontend (HTML/JS), deploy to Vercel:

#### Step 1: Create Web Interface

Create `public/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DocGen - AI Documentation Generator</title>
    <style>
        /* Add your styles */
    </style>
</head>
<body>
    <h1>DocGen - AI Documentation Generator</h1>
    <!-- Add your interface -->
</body>
</html>
```

#### Step 2: Deploy to Vercel

```bash
npm install -g vercel
vercel login
vercel --prod
```

---

## 🔧 Environment Variables

If using IBM Bob API key, set environment variables:

### Streamlit Cloud:
1. Go to app settings
2. Add secret: `BOB_API_KEY = your_key_here`

### Replit:
1. Go to "Secrets" tab
2. Add: `BOB_API_KEY = your_key_here`

### Vercel:
```bash
vercel env add BOB_API_KEY
```

---

## 🧪 Testing Your Deployment

Before submitting, test your deployed app:

1. **Functionality Test:**
   - Upload sample Python files
   - Generate documentation
   - Verify output quality
   - Test download buttons

2. **Performance Test:**
   - Try with different file sizes
   - Check loading times
   - Verify error handling

3. **Accessibility Test:**
   - Open in different browsers
   - Test on mobile devices
   - Check all links work

---

## 📝 Deployment Checklist

- [ ] Streamlit app created (`streamlit_app.py`)
- [ ] Requirements updated with all dependencies
- [ ] Code pushed to GitHub (public repo)
- [ ] App deployed to chosen platform
- [ ] Demo URL tested and working
- [ ] Environment variables configured (if needed)
- [ ] Error handling tested
- [ ] Mobile responsiveness checked
- [ ] Demo URL added to README.md
- [ ] Demo URL ready for submission form

---

## 🆘 Troubleshooting

### Issue: Streamlit app won't start
```bash
# Test locally first
streamlit run streamlit_app.py

# Check logs in Streamlit Cloud dashboard
# Verify all imports are in requirements.txt
```

### Issue: Import errors
```python
# Add to top of streamlit_app.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
```

### Issue: File upload not working
- Check file size limits (Streamlit: 200MB default)
- Verify file type restrictions
- Test with small files first

### Issue: IBM Bob API not working
- Verify API key is set correctly
- Check if running in mock mode (should show warning)
- Test with sample_project locally first

---

## 💡 Pro Tips

1. **Test locally first** before deploying
2. **Use sample files** for demo screenshots
3. **Add loading indicators** for better UX
4. **Include error messages** that are helpful
5. **Make it visually appealing** - first impressions matter
6. **Add your GitHub link** prominently
7. **Include usage instructions** in the UI
8. **Test the download feature** thoroughly

---

## 📊 Demo Best Practices

For your video demo:
1. Show the deployed URL
2. Upload sample files
3. Generate documentation
4. Show the output quality
5. Highlight AI-generated examples
6. Download the results
7. Show it's fast and easy to use

---

**Your demo URL is a critical part of the submission - make sure it works perfectly! 🚀**