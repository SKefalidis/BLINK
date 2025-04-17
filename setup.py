#!/usr/bin/env python3
from setuptools import setup, find_packages
import os

# Automatically add __init__.py to all directories missing it
def add_init_files():
    for root, dirs, files in os.walk("."):
        # Only add __init__.py to folders that contain Python files but lack it
        if "__init__.py" not in files and any(f.endswith(".py") for f in files):
            with open(os.path.join(root, "__init__.py"), "w"):
                pass

# Call this function before running setup
add_init_files()

# Read the README file for the long description
with open("README.md") as f:
    readme = f.read()

# The actual setup
setup(
    name="BLINK",
    version="0.1.0",
    description="BLINK: Better entity LINKing",
    url="",  # TODO
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds all packages
    setup_requires=["setuptools>=18.0"],
    install_requires=[
        "torch>=1.2.0",
        "pysolr>=3.8.1",
        "emoji>=0.5.3",
        "regex>=2019.8.19",
        "matplotlib>=3.1.0",
        "tqdm>=4.32.1",
        "nltk>=3.4.4",
        "numpy>=1.17.2",
        "segtok>=1.5.7",
        "flair>=0.4.3",
        "pytorch-transformers>=1.2.0",
        "colorama>=0.4.3",
        "termcolor>=1.1.0",
        "faiss-cpu>=1.6.1",
    ],
)
