import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Text-Summarization-Project"
AUTHOR_NAME = "manjit-baishya-datascience"
SRC_REPO = "text-summarizer"
AUTHOR_EMAIL = "manjitbaishya01@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    email=AUTHOR_EMAIL,
    description="An end-to-end text summarization project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)