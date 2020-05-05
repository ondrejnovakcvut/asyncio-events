#!/usr/bin/env python

from setuptools import setup, find_packages

DESCRIPTION = "Events inspired by C# EventHandler supporting async methods"
LONG_DESCRIPTION = open('README.rst').read()
VERSION = __import__('asyncio-events').__version__

setup(
    name='asyncio-events',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Ondrej Novak',
    author_email='ondrej.novak.2@cvut.cz',
    url='https://github.com/ondrejnovakcvut/asyncio-events',
    license="BSD",
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    test_suite="asyncio-events.tests",
    install_requires=['aiounittest'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
)
