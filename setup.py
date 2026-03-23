"""
Setup configuration for Finance Tracker Models package.
This allows the models to be installed as a pip package and shared across projects.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="finance-tracker-models",
    version="0.1.1",
    author="Aitor Fernandez",
    author_email="your-email@example.com",
    description="Shared SQLAlchemy models for Finance Tracker projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/finance-tracker-models",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "sqlalchemy>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/finance-tracker-models/issues",
        "Source": "https://github.com/yourusername/finance-tracker-models",
    },
)
