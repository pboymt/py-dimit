#!/usr/bin/env python

from setuptools import setup, find_packages, Command
import os
from os import path
import sys
from shutil import rmtree

# Package meta-data.
NAME = 'dimit'
DESC = 'Dimension of a quantity in Python language.'
URL = 'https://github.com/pboymt/dimit'
EMAIL = os.getenv('PypiEmail')
AUTHOR = os.getenv('PypiAuthor')
REQUIRES_PYTHON = '>=3.9.0'
VERSION: str = None  # '0.0.1'

# What packages are required for this module to be executed?
REQUIREMENTS = []

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['numpy'],
}

cwd = os.path.abspath(path.dirname(__file__))

try:
    with open(path.join(cwd, 'README.md'), encoding='utf-8') as f:
        LONG_DESC = f.read()
    with open(path.join(cwd, 'LICENSE'), encoding='utf-8') as f:
        LICENSE = f.read()
except FileNotFoundError:
    LONG_DESC = DESC
    LICENSE = 'GPLv3'

ABOUT = {}

if not VERSION:
    with open(path.join(cwd, NAME, '__version__.py')) as f:
        exec(f.read(), ABOUT)
else:
    ABOUT['__version__'] = VERSION


class TestCommand(Command):
    """
    Run tests
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('pytest')


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(cwd, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            '{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(ABOUT['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name=NAME,
    version=ABOUT['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESC,
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    requires=REQUIREMENTS,
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    }
)
