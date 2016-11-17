#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='macostk',
    version='0.1.0',
    description="A collection of python functions and classes to help with administering macOS",
    long_description=readme + '\n\n' + history,
    author="Kyle Crawshaw",
    author_email='kyle@kylecrawshaw.com',
    url='https://github.com/kylecrawshaw/macostk',
    packages=[
        'macostk',
    ],
    package_dir={'macostk':
                 'macostk'},
    entry_points={
        'console_scripts': [
            'macostk=macostk.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='macostk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
