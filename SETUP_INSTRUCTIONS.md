# DocGen - Complete Setup Instructions

## ⚠️ IMPORTANT: Python Installation Required

Your system does not have Python installed. You need to install Python before proceeding.

---

## Step 1: Install Python

### Windows Installation:

1. **Download Python:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download Python 3.11 or 3.12 (latest stable version)
   - Choose "Windows installer (64-bit)"

2. **Install Python:**
   - Run the downloaded installer
   - ⚠️ **IMPORTANT:** Check "Add Python to PATH" at the bottom
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation:**
   Open PowerShell and run:
   ```powershell
   python --version
   ```
   Should show: `Python 3.11.x` or `Python 3.12.x`

---

## Step 2: Install Project Dependencies

Once Python is installed, open PowerShell in the project directory and run:

```powershell
# Install required packages
python -m pip install --upgrade pip
python -m pip install click
python -m pip install streamlit
python -m pip install weasyprint  # Optional, for PDF export
```

Or install all at once:
```powershell
python -m pip install -r requirements.txt
```

---

## Step 3: Test the Application

### Test CLI Version:
```powershell
# Test on sample project
python main.py ./sample_project

# Test with all formats
python main.py ./sample_project --format all --output ./demo_output

# Check the output
dir demo_output
```

You should see:
- `sample_project_docs.md`
- `sample_project_docs.html`
- `sample_project_docs.pdf` (if weasyprint installed)

### Test Streamlit Web App:
```powershell
# Run Streamlit locally
streamlit run streamlit_app.py
```

This will open a browser window at `http://localhost:8501`

---

## Step 4: Export IBM Bob Report

**CRITICAL for hackathon submission!**

1. Open IBM Bob VS Code extension
2. Go to task/session history
3. Select all DocGen-related tasks
4. Click "Export Report"
5. Save as `IBM_BOB_REPORT.md` in project root
6. Verify the file was created:
   ```powershell
   dir IBM_BOB_REPORT.md
   ```

If you cannot export from IBM Bob:
- Use the template: `IBM_BOB_REPORT_TEMPLATE.md`
- Fill in your actual session details
- Rename to `IBM_BOB_REPORT.md`

---

## Step 5: Update README with Demo Links

Edit `README.md` and add:

```markdown
## 🚀 Live Demo

- **Web App:** [Your Streamlit URL]
- **Video Demo:** [Your video URL]
- **Presentation:** [Your slides URL]

## 📊 IBM Bob Integration

This project was developed with IBM Bob AI assistance. See [IBM_BOB_REPORT.md](./IBM_BOB_REPORT.md) for complete development history.

## 🏆 Hackathon Submission

Built for IBM Bob Hackathon 2026 on lablab.ai
```

---

## Step 6: Deploy to Streamlit Cloud

### Prerequisites:
- GitHub account
- Project pushed to GitHub (public repository)

### Deployment Steps:

1. **Push to GitHub:**
   ```powershell
   git add .
   git commit -m "Add Streamlit web interface"
   git push origin main
   ```

2. **Deploy to Streamlit:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file: `streamlit_app.py`
   - Click "Deploy"

3. **Get Your URL:**
   - Wait for deployment (2-5 minutes)
   - Copy the URL (e.g., `https://yourusername-docgen.streamlit.app`)
   - Test the URL in your browser
   - Use this URL in your hackathon submission

---

## Step 7: Create Submission Materials

### A. Cover Image (30 minutes)
Use Canva or similar tool:
- Size: 1920x1080 (16:9 ratio)
- Include: "DocGen" title, tagline, IBM Bob logo
- Save as: `cover_image.png`

### B. Presentation Slides (1-2 hours)
Follow the structure in `SUBMISSION_PLAN.md`:
- 10-12 slides covering problem, solution, tech, market
- Export as PDF: `docgen_presentation.pdf`

### C. Video Demo (30-60 minutes)
Follow the script in `SUBMISSION_PLAN.md`:
- Max 5 minutes
- Show: intro, slides, live demo, closing
- Record with OBS Studio or Loom
- Save as: `docgen_demo.mp4`

---

## Step 8: Prepare Submission Text

### Short Description (255 chars):
```
DocGen uses IBM Bob AI to automatically generate comprehensive Python documentation. Parse code → AI generates docstrings → Export as Markdown, HTML, or PDF. Save 70% of documentation time with consistent, example-rich docs.
```

### Long Description:
See `SUBMISSION_PLAN.md` for the complete long description (already written!)

### Tags:
- **Technology:** IBM Bob, Python, AI/ML, Developer Tools, Documentation
- **Category:** Developer Tools, Productivity, AI-Powered

---

## Step 9: Final Checklist

Before submitting to lablab.ai:

- [ ] Python installed and working
- [ ] All dependencies installed
- [ ] Application tested locally
- [ ] IBM Bob report exported (`IBM_BOB_REPORT.md`)
- [ ] Cover image created (`cover_image.png`)
- [ ] Presentation slides created (`docgen_presentation.pdf`)
- [ ] Video recorded (`docgen_demo.mp4`)
- [ ] GitHub repository is PUBLIC
- [ ] README updated with demo links
- [ ] Streamlit app deployed and tested
- [ ] All submission text prepared
- [ ] All links verified and working

---

## Step 10: Submit to lablab.ai

1. Go to the IBM Bob Hackathon page on lablab.ai
2. Click "Submit Project"
3. Fill in all fields:
   - Project title: **DocGen**
   - Short description: (from above)
   - Long description: (from SUBMISSION_PLAN.md)
   - Cover image: Upload `cover_image.png`
   - Video: Upload `docgen_demo.mp4`
   - Slides: Upload `docgen_presentation.pdf`
   - GitHub URL: Your public repo URL
   - Demo URL: Your Streamlit app URL
   - Tags: Select from list above
4. Review everything carefully
5. Click "Submit"
6. 🎉 Celebrate!

---

## Troubleshooting

### Issue: "Python not found"
- Reinstall Python with "Add to PATH" checked
- Restart PowerShell after installation
- Try `py` instead of `python`

### Issue: "pip not found"
```powershell
python -m ensurepip --upgrade
```

### Issue: "Module not found"
```powershell
python -m pip install --upgrade -r requirements.txt
```

### Issue: Streamlit won't start
```powershell
python -m pip install --upgrade streamlit
streamlit run streamlit_app.py
```

### Issue: Can't deploy to Streamlit Cloud
- Ensure repository is public
- Check requirements.txt is complete
- Verify streamlit_app.py is in root directory
- Check Streamlit Cloud logs for errors

---

## Quick Command Reference

```powershell
# Install dependencies
python -m pip install -r requirements.txt

# Test CLI
python main.py ./sample_project --format all

# Run Streamlit locally
streamlit run streamlit_app.py

# Push to GitHub
git add .
git commit -m "Ready for submission"
git push origin main

# Check Python version
python --version

# Check installed packages
python -m pip list
```

---

## Time Estimates

- **Python Installation:** 10 minutes
- **Dependency Installation:** 5 minutes
- **Testing Application:** 15 minutes
- **IBM Bob Report Export:** 10 minutes
- **Cover Image Creation:** 30 minutes
- **Presentation Slides:** 1-2 hours
- **Video Recording:** 30-60 minutes
- **Deployment:** 30 minutes
- **Submission:** 15 minutes

**Total:** 4-6 hours

---

## Need Help?

- Review `SUBMISSION_PLAN.md` for detailed guidance
- Check `QUICK_START_GUIDE.md` for quick reference
- See `DEPLOYMENT_GUIDE.md` for deployment options
- Join hackathon Discord/Slack for community support

---

**You've got this! Follow these steps and you'll have a complete, professional submission. Good luck! 🚀**