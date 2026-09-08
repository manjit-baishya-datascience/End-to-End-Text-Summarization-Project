import os
from pathlib import Path
import logging

# Logging template
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

# Declaring project name
project_name = "text_summarizer"

# Files that are to be created
list_of_files = [
    ".github/workflows/.gitkeep",                      # Keeps CI/CD workflows folder tracked in git

    f"src/{project_name}/__init__.py",                 # Marks src package as installable local package
    f"src/{project_name}/components/__init__.py",      # Package init for core components (data ingestion, transformation, etc.)
    f"src/{project_name}/utils/__init__.py",           # Package init for utility functions
    f"src/{project_name}/utils/common.py",             # Common/reusable helper functions (YAML read, dir creation, etc.)
    f"src/{project_name}/logging/__init__.py",         # Custom logging setup for the project
    f"src/{project_name}/config/__init__.py",          # Package init for configuration handling
    f"src/{project_name}/config/configuration.py",     # Reads config/params files and returns config objects
    f"src/{project_name}/pipeline/__init__.py",        # Package init for pipeline stages (training/prediction pipelines)
    f"src/{project_name}/entity/__init__.py",          # Package init for entity classes (config data structures)
    f"src/{project_name}/constants/__init__.py",       # Stores constant values (file paths, etc.) used across project

    "config/config.yaml",                              # Project configuration (paths, sources, artifacts)
    "params.yaml",                                     # Model/training hyperparameters

    "app.py",                                          # Entry point for web app / API serving
    "main.py",                                         # Entry point to run the full training pipeline
    "setup.py",                                        # File for entire app setup

    "Dockerfile",                                      # Docker image build instructions for deployment
    "requirements.txt",                                # Python dependencies list

    "research/trials.ipynb",                           # Jupyter notebook for experimentation and prototyping

    "README.md",                                       # Project overview and documentation
    ".env",                                            # Environment variables (secrets, API keys) - not committed
    ".gitignore",                                      # Files/folders excluded from git tracking
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} already exists")