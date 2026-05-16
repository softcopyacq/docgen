# DocGen - Quick Start Guide for Hackathon Submission

## 🚀 Immediate Action Items

### Step 1: Install & Test (15 minutes)
```bash
# Install dependencies
pip install click
pip install weasyprint  # Optional for PDF

# Test the application
python main.py ./sample_project --format all --output ./demo_output

# Verify outputs
ls demo_output/
# Should see: sample_project_docs.md, sample_project_docs.html, sample_project_docs.pdf
```

### Step 2: Export IBM Bob Report (10 minutes)
**CRITICAL**: This is a mandatory requirement!

1. Open IBM Bob VS Code extension
2. Go to task/session history
3. Select all DocGen-related tasks
4. Click "Export Report"
5. Save as `IBM_BOB_REPORT.md` in project root
6. Add reference to README.md

### Step 3: Create Submission Materials (2-3 hours)

#### A. Cover Image (30 minutes)
- Use Canva or Figma
- Size: 1920x1080 (16:9)
- Include: "DocGen" title, "AI-Powered Documentation Generator" tagline
- Save as: `cover_image.png`

#### B. Slide Presentation (1 hour)
Use the structure from SUBMISSION_PLAN.md:
- 10-12 slides
- Cover: Problem, Solution, Tech Stack, Market, Competition, Future
- Export as: `docgen_presentation.pdf`

#### C. Video Script (30 minutes)
Follow the script in SUBMISSION_PLAN.md:
- Introduction (30s)
- Problem & Solution (1min)
- Slides walkthrough (2min)
- Live demo (1.5min)
- Closing (30s)

#### D. Record Video (30 minutes)
- Use OBS Studio, Loom, or screen recorder
- Show terminal demo
- Keep under 5 minutes
- Save as: `docgen_demo.mp4`

### Step 4: Deploy Demo (30 minutes)

**Option A: Streamlit (Easiest)**
```bash
# Create streamlit_app.py (see SUBMISSION_PLAN.md for code)
pip install streamlit
streamlit run streamlit_app.py

# Deploy to Streamlit Cloud
# 1. Push to GitHub
# 2. Go to share.streamlit.io
# 3. Connect repo and deploy
```

**Option B: Replit**
1. Import GitHub repo to Replit
2. Make public
3. Share URL

### Step 5: Prepare Submission Text (20 minutes)

**Short Description (255 chars max):**
```
DocGen uses IBM Bob AI to automatically generate comprehensive Python documentation. Parse code → AI generates docstrings → Export as Markdown, HTML, or PDF. Save 70% of documentation time with consistent, example-rich docs.
```

**Long Description:**
See SUBMISSION_PLAN.md for full text (already written!)

**Tags:**
- Technology: IBM Bob, Python, AI/ML, Developer Tools, Documentation
- Category: Developer Tools, Productivity, AI-Powered

### Step 6: GitHub Setup (15 minutes)
```bash
# Ensure repo is PUBLIC
# Add IBM_BOB_REPORT.md
# Update README.md with:
# - IBM Bob report reference
# - Demo URL
# - Video link
# - Hackathon badge

git add .
git commit -m "Prepare for lablab.ai submission"
git push origin main
```

### Step 7: Submit to lablab.ai (15 minutes)
1. Go to lablab.ai hackathon page
2. Fill in submission form:
   - Project title: DocGen
   - Short description: (from above)
   - Long description: (from SUBMISSION_PLAN.md)
   - Cover image: Upload `cover_image.png`
   - Video: Upload `docgen_demo.mp4`
   - Slides: Upload `docgen_presentation.pdf`
   - GitHub URL: Your public repo
   - Demo URL: Your Streamlit/Replit URL
   - Tags: Select from above list
3. Review everything
4. Submit! 🎉

---

## ⏱️ Time Estimate
- **Minimum**: 4-5 hours (if you work efficiently)
- **Recommended**: 6-8 hours (for quality materials)
- **Ideal**: Spread over 2-3 days

---

## 📋 Final Checklist

Before submitting, verify:
- [ ] Application runs without errors
- [ ] IBM Bob report exported and in repo
- [ ] Cover image created (16:9, PNG/JPG)
- [ ] Slide presentation complete (PDF)
- [ ] Video recorded and under 5 minutes (MP4)
- [ ] Demo deployed and accessible
- [ ] GitHub repo is PUBLIC
- [ ] README updated with all links
- [ ] Short description ≤255 characters
- [ ] Long description ≥100 words
- [ ] All tags selected
- [ ] All links tested and working

---

## 🆘 Troubleshooting

**Issue: Application won't run**
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install --upgrade click weasyprint
```

**Issue: Can't export IBM Bob report**
- Check IBM Bob extension is installed
- Look for export button in task history
- If unavailable, create manual report documenting Bob's assistance

**Issue: Video too large**
- Compress using HandBrake or online tools
- Target: Under 100MB
- Resolution: 1080p is fine, 720p acceptable

**Issue: Demo deployment fails**
- Try different platform (Streamlit vs Replit)
- Check requirements.txt is complete
- Verify all imports work

---

## 💡 Pro Tips

1. **Start with testing**: Make sure app works before creating materials
2. **Record demo early**: You can re-record if needed
3. **Use templates**: Canva has great presentation templates
4. **Practice your pitch**: Record video multiple times if needed
5. **Get feedback**: Have someone review your materials
6. **Submit early**: Don't wait until deadline
7. **Keep it simple**: Clear communication > fancy effects

---

## 📞 Need Help?

- Review SUBMISSION_PLAN.md for detailed guidance
- Check lablab.ai hackathon guide (available when hackathon starts)
- Join hackathon Discord/Slack for community support
- IBM Bob documentation for technical questions

---

**You've got this! 🚀 Good luck with your submission!**