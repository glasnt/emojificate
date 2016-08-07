import re
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'emojificate', '__init__.py'), encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name='emojificate',
    version=version,
    description='A Python implementation of a concept of using fallback images, alt text, title text and aria labels to represent emoji in HTML code in a more accessible method.',
    long_description=long_description,
    url='https://github.com/glasnt/emojificate',
    author='Katie McLaughlin',
    author_email='katie@glasnt.com',
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
    keywords='emoji accessibility a11y',
    packages=find_packages(exclude=['docs', 'test']),
)
