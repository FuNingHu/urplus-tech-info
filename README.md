# UR+ Technical Information Documentation

This repository contains the technical documentation for UR+ product development, updated for PolyScope X.

## Overview

This document outlines the requirements and processes for developing, testing, and approving UR+ products to ensure seamless integration with Universal Robots.

## Contents

- **Key Updates for PolyScope X** - Important changes for PolyScope X development
- **Technical Resources** - Support resources and contact information
- **Technical Scoping** - Scoping process for UR+ product development
- **Development Deliverables** - Required deliverables for certification
- **Testing Methodology** - Testing and validation procedures
- **Self-Testing Checkpoint** - Pre-test checklist for partners

## Building the Documentation

### Prerequisites

1. Install Python 3.8+
2. Install required packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install sphinx sphinx-rtd-theme sphinx-multiversion
```

### Build HTML Locally

```bash
cd docs

# Windows (PowerShell)
.\make.bat html

# Linux/Mac
make html
```

The built documentation will be available in `docs/build/html/`.

### View Documentation Locally

Open `docs/build/html/index.html` in your browser.

### Clean Build

To clean previous build files:

```bash
cd docs

# Windows (PowerShell)
.\make.bat clean

# Linux/Mac
make clean
```

## Deploying to GitHub Pages

### Automatic Deployment (GitHub Actions)

This repository is configured with GitHub Actions for automatic deployment. When you push to the `main` branch, the documentation will be automatically built and deployed to GitHub Pages.

The workflow file is located at `.github/workflows/docs.yml`.

### Manual Deployment Steps

1. **Build the documentation:**

   ```bash
   cd docs
   .\make.bat html
   ```

2. **Commit and push changes:**

   ```bash
   git add .
   git commit -m "Update documentation"
   git push origin main
   ```

3. **Wait for GitHub Actions** to complete the build and deployment.

4. **Access the documentation** at: https://funinghu.github.io/urplus-tech-info/

### Enabling GitHub Pages

If GitHub Pages is not enabled:

1. Go to your repository on GitHub
2. Navigate to **Settings** > **Pages**
3. Under "Source", select **gh-pages** branch
4. Click **Save**

## Project Structure

```
URplus_tech_info/
├── docs/
│   ├── source/
│   │   ├── _static/          # Custom CSS/JS files
│   │   ├── _templates/       # Custom templates
│   │   ├── images/           # Documentation images
│   │   ├── conf.py           # Sphinx configuration
│   │   ├── index.rst         # Main page
│   │   └── *.rst             # Documentation pages
│   ├── build/                # Build output (generated)
│   ├── Makefile              # Linux/Mac build script
│   └── make.bat              # Windows build script
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions workflow
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Editing Documentation

1. Edit `.rst` files in `docs/source/`
2. Build locally to preview changes
3. Commit and push to trigger deployment

### RST Quick Reference

```rst
# Heading 1
=========

## Heading 2
-----------

**Bold text**

*Italic text*

`inline code`

.. code-block:: python

   print("Hello World")

.. note::
   This is a note.

.. warning::
   This is a warning.
```

## License

© 2026 Universal Robots A/S. All rights reserved.

