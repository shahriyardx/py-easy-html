from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

current_directory = Path(__file__).parent.resolve()

long_description = (current_directory / "README.md").read_text(encoding="utf-8")

vpath = current_directory / "easy_html" / "_version.py"
spec = spec_from_file_location(vpath.name[:-3], vpath)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

setup(
    name="py-easy-html",
    version=mod.__version__,
    description="Generate HTML using python and also convert to PDF.",  # Optional
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/py-easy-html",
    author="Md Shahriyar Alam",
    author_email="contact@shahriyar.dev",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="HTML Generator, HTML to PDF,",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=requirements,
    project_urls={
        "Bug Reports": "https://github.com/shahriyardx/py-easy-html/issues",
        "Source": "https://github.com/shahriyardx/py-easy-html/",
    },
)
