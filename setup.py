from __future__ import with_statement

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), 'r') as f:
    requirements = [r.strip() for r in f.read().splitlines()]

setup(
    name='maropost_api',
    version='0.1',
    packages=['maropost_api'],
    url='',
    author='PowerToFly.com',
    author_email='developers@powertofly.com',
    description='maropost.com API wrapper',
    include_package_data=True,
    install_requires=requirements
)
