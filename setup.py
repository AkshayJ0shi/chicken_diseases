# We want our model to be a local package

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# IMP : Here SRC_REPO and REPO_NAME on github happen to be the same
# Ideally, "name" in setuptools should point to SRC_REPO, not REPO_NAME

__version__ = "0.0.0"
REPO_NAME = "chicken_diseases"
AUTHOR_USERNAME = "AkshayJ0shi"
AUTHOR_EMAIL = "akshayjoshi1117@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Local package for CNN classifier",
    long_description = long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)