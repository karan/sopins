import os
import sys
from setuptools import setup, find_packages

setup(
    name='sopins',
    version='0.0.1',
    description='Social badges on the fly.',
    author='Karan Goel',
    author_email='karan@goel.im',
    url='https://github.com/karan/sopins',
    packages=find_packages(),
    zip_safe=False,
    keywords='social twitter facebook badges pins',
    install_requires=[
        'flask>=0.10.1',
        'requests>=2.2.1',
        'simplejson>=3.3.3',
        'gunicorn==18.0',
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
