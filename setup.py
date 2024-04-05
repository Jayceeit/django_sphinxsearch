import os
import re
import subprocess
from pathlib import Path

from setuptools import setup  # type: ignore

with open('README.md') as f:
    long_description = f.read()

package_name = 'django_sphinxsearch'

setup(
    name=package_name,
    version=__import__('sphinxsearch').VERSION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'sphinxsearch',
        'sphinxsearch.backend',
        'sphinxsearch.backend.sphinx',
    ],
    url='http://github.com/tumb1er/django_sphinxsearch',
    license='Beerware',
    author='tumbler',
    author_email='zimbler@gmail.com',
    description='Sphinxsearch database backend for django>=3.0',
)
