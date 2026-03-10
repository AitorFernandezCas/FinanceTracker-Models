"""
Base SQLAlchemy configuration for shared models.
This module is app-independent and can be used in any project.
"""
from sqlalchemy.orm import declarative_base

# Declarative base for all models
Base = declarative_base()
