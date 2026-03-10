# Quick Start: Extract Models as Standalone Package

This guide shows how to create a standalone, shareable models package from the Finance Tracker models.

## Step 1: Create Repository Structure

```bash
# Create new directory for models package
mkdir finance-tracker-models
cd finance-tracker-models

# Initialize git
git init

# Add these files from the current models/ directory:
# - models/
# - setup.py
# - pyproject.toml
# - MANIFEST.in  
# - README.md
```

## Step 2: Create Package Files

Your package structure should look like:
```
finance-tracker-models/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── deudas.py
│   ├── inmuebles.py
│   ├── liquidez.py
│   ├── hist_compra_instrumentos_financieros.py
│   ├── README.md
│   └── master/
│       ├── __init__.py
│       ├── maestro_activos_financieros.py
│       ├── maestro_bancos.py
│       └── maestro_divisas.py
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── README.md
├── LICENSE
└── .gitignore
```

## Step 3: Create .gitignore

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/
EOF
```

## Step 4: Install Locally (for testing)

```bash
# Install in development mode
pip install -e .

# Now you can import from anywhere:
# from models import Deudas, Inmuebles, Liquidez, ...
```

## Step 5: Publish to GitHub

```bash
# Add GitHub remote
git remote add origin https://github.com/yourusername/finance-tracker-models.git

# Create commits
git add .
git commit -m "Initial commit: Finance Tracker Models"
git push -u origin main
```

## Step 6: Use in Other Projects

### Option A: Install from GitHub (using pip)
```bash
pip install git+https://github.com/yourusername/finance-tracker-models.git
```

### Option B: Install from PyPI (after publishing)
```bash
pip install finance-tracker-models
```

### Option C: Add as Git Submodule
```bash
git submodule add https://github.com/yourusername/finance-tracker-models.git vendor/finance-models
pip install -e vendor/finance-models
```

## Step 7: Use Models in New Project

```python
# new_project/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base, Deudas, Inmuebles, Liquidez

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://..."
    
    db.init_app(app)
    db.metadata = Base.metadata
    
    with app.app_context():
        db.create_all()
    
    return app
```

## Publishing to PyPI (Optional)

If you want to make it publicly available on PyPI:

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to PyPI (requires account)
python -m twine upload dist/*
```

Then anyone can install with:
```bash
pip install finance-tracker-models
```

## Version Management

Update version in multiple places:
- `setup.py`: `version="x.y.z"`
- `pyproject.toml`: `version = "x.y.z"`
- `models/__init__.py`: `__version__ = "x.y.z"` (optional)

Then tag releases:
```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

---

**Now your models are:** ✅ Independent  ✅ Shareable  ✅ Version controlled  ✅ Distributable
