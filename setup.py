#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='beets-drop',
    version='0.0.1',
    namespace_packages=['beetsplug'],
    packages=['beetsplug'],
    author='Vincent Mazenod',
    author_email='vmazenod@gmail.com',
    description='Beets plugin to drop incomplete and unclassified items in particular folders',
    long_description=open('README.rst').read(),
    url='https://github.com/mazenovi/beets-drop',
    install_requires=[
        'beets'
    ]
)
