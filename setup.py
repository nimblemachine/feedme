# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import FeedMe
version = FeedMe.__version__

setup(
    name='FeedMe',
    version=version,
    author='',
    author_email='andrew@nimblemachine.com',
    packages=[
        'FeedMe',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['FeedMe/manage.py'],
)