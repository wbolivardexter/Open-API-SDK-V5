# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import os
import sys
from shutil import rmtree

from setuptools import Command
from setuptools import find_packages
from setuptools import setup


# Package meta-data.
NAME = 'okx'
SRC_DIR = 'okx'
DESCRIPTION = 'A unofficial python API wrapper developed to interact with the OKX V5 API.'
URL = 'https://github.com/wbolivardexter/Open-API-SDK-V5'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    'requests',
    'websockets==6.0',
]

# What packages are required only for tests?
TESTS = [
    'mock==2.0.0',
    'pytest==4.3.1',
]

# What packages are optional?
EXTRAS = {
    'flake8': [
        'flake8==3.6.0',
        'flake8-isort==2.6.0',
        'isort==4.3.4',
        'testfixtures==6.3.0',
    ],
    'tests': TESTS,
}

here = os.path.abspath(os.path.dirname(__file__))


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!

try:
    # Python 3 will raise FileNotFoundError instead of IOError
    FileNotFoundError = IOError
except NameError:
    pass

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, SRC_DIR, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


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
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=REQUIRED,
    tests_require=TESTS,
    extras_require=EXTRAS,
    # $ setup.py upload support.
    cmdclass={
        'upload': UploadCommand,
    },
)