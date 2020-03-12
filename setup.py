import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='drf-problems',
    version=get_version('drf_problems'),
    description='Never liked DRF plain old errors? Forget that and accept RFC 7807 - Problem Details!',
    long_description=README,
    long_description_content_type="text/markdown",
    author='shivanshs9',
    author_email='shivanshs9@gmail.com',
    url='https://github.com/shivanshs9/drf-problems/',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'Django>=1.6',
        'djangorestframework>=3.0.0'
    ]
)
