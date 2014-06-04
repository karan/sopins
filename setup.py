import os
import sys
from setuptools import setup, find_packages

setup(
    name='sopins',
    version='0.0.0',
    description='Badges for your site to display social buttons.',
    author='Karan Goel',
    author_email='karan@goel.im',
    url='https://github.com/karan/sopins',
    packages=find_packages(),
    zip_safe=False,
    keywords='social twitter facebook badges pins',
    install_requires=[
        'Twisted>=13.2.0',
        'klein>=0.2.3',
        'requests>=2.2.1',
        'simplejson>=3.3.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
