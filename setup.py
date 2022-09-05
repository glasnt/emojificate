import re
from setuptools import setup, find_packages
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="emojificate",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Convert emoji in HTML to fallback images, alt text, title text, and aria labels.",
    long_description=long_description,
    url="https://github.com/glasnt/emojificate",
    author="Katie McLaughlin",
    author_email="katie@glasnt.com",
    license="New BSD",
    install_requires=["emoji", "grapheme", "requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
    ],
    keywords="emoji accessibility a11y",
    packages=find_packages(exclude=["docs", "test"]),
)
