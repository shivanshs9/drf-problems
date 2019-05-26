import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='drf-problems',
    version='0.1',
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
