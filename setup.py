"""
    mux
    ```
    an elegant handler for python terminal logging
"""

import re
import ast
from setuptools import setup, find_packages

# version
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('mux/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')
    ).group(1)))


setup(
    name='mux-handler',
    version=version,
    packages=find_packages(),
    url='https://github.com/neo1218/mux',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='an elegant handler for python terminal logging',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pygments',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
