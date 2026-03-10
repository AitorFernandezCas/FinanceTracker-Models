# Shared Finance Tracker Models Package

This models package is designed to be **app-independent and shareable** across multiple projects.

## Architecture

### Before (App-Dependent)
```
Models depend on app instance
from app import db  ❌
```

### After (Independent)
```
Models use SQLAlchemy directly
from sqlalchemy import Column, Integer, String, DateTime
from .base import Base  ✅
```

## Structure

```
models/
├── __init__.py              # Main package exports
├── base.py                  # Declarative base (shared foundation)
├── deudas.py
├── inmuebles.py
├── liquidez.py
├── hist_compra_instrumentos_financieros.py
└── master/
    ├── __init__.py
    ├── maestro_activos_financieros.py
    ├── maestro_bancos.py
    └── maestro_divisas.py
```

## How It Works

### 1. **Base Model** (`base.py`)
All models inherit from a shared `Base` (SQLAlchemy's `declarative_base`):
```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

### 2. **Individual Models**
Each model now imports SQLAlchemy types directly:
```python
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Deudas(Base):
    __tablename__ = 'deudas'
    id_deuda = Column(Integer, primary_key=True)
    # ... rest of the model
```

### 3. **Easy Imports** (`__init__.py`)
All models are exported from a single package:
```python
from models import Deudas, Inmuebles, Liquidez, MaestroBancos, ...
```

### 4. **App Integration** (`app.py`)
The Flask app imports models and registers their metadata:
```python
from models import Base, Deudas, Inmuebles, ...

db = SQLAlchemy()

# ... in create_app():
db.init_app(app)
db.metadata = Base.metadata  # 👈 Key: Register models with SQLAlchemy
```

---

## Using Models in Your Current App

### Import Models
```python
from models import Deudas, Inmuebles, Liquidez

# Use in services/routes
deuda = Deudas(id_deuda=1, valor_total=1000.0)
```

### Query Models
```python
from app import db
from models import Deudas

# Query still works normally
todos_deudas = db.session.query(Deudas).all()
```

---

## Extracting as a Standalone Package

To use these models in other projects:

### Option 1: **Git Submodule**
```bash
git submodule add <repo-url> shared-models
```

### Option 2: **pip Package**
Create a `setup.py`:
```python
from setuptools import setup, find_packages

setup(
    name="finance-tracker-models",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=2.0.0",
    ],
)
```

Install: `pip install -e git+<repo-url>#egg=finance-tracker-models`

### Option 3: **Copy to Shared Location**
Copy the `models/` folder to another project and import directly.

---

## Using in Another Project

### Example: New Project Using Finance Models

```python
# new_project/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base, Deudas, Inmuebles, Liquidez  # Import your models

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://..."
    db.init_app(app)
    db.metadata = Base.metadata  # Register metadata
    
    with app.app_context():
        db.create_all()  # Create tables
    
    return app
```

---

## Key Benefits

✅ **No App Dependency** - Models don't know about Flask  
✅ **Reusable** - Use same models across projects  
✅ **Type Safe** - SQLAlchemy provides full IDE support  
✅ **Database Agnostic** - Works with any SQL database  
✅ **Version Control** - Easy to track model changes  
✅ **Testing** - Easy to mock/test without app context  

---

## Migration Guide

Your existing code continues to work:
- ✅ `db.session.query(Deudas).all()` - Still works
- ✅ `db.session.add(deuda)` - Still works  
- ✅ Flask-Migrate - Still compatible
- ✅ Relationships - Add with `relationship()` as needed

No breaking changes! 🎉

---

## Next Steps

1. **Add Relationships** (if needed):
   ```python
   from sqlalchemy.orm import relationship
   
   class Deudas(Base):
       __tablename__ = 'deudas'
       
       # Add relationships
       banco = relationship("MaestroBancos", ...)
   ```

2. **Create a Separate Repository**:
   ```bash
   mkdir finance-tracker-models
   cp -r models/* finance-tracker-models/
   cd finance-tracker-models
   git init
   ```

3. **Publish to pip** (optional):
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

---

