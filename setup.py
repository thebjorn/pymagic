# -*- coding: utf-8 -*-

import setuptools
from distutils.core import setup

setup(
    name='magicmethods',
    version='0.1.3',
    py_modules=['magicmethods'],
    long_description=open("README.rst").read(),
    url='https://github.com/thebjorn/pymagic',
    license='LGPL',
    author='bjorn',
    author_email='bp@datakortet.no',
    description='Simple, importable, list(s) of python magic method names.',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
