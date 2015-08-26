#!/usr/bin/env python

import re
from setuptools import setup


READMEFILE = 'README.rst'
VERSIONFILE = 'pytest_wholepath.py'
VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""


def get_version():
    version_file = open(VERSIONFILE, 'rt').read()
    return re.search(VSRE, version_file, re.M).group(1)


setup(
    name='pytest-wholepath',
    version=get_version(),
    description=open(READMEFILE).read(),
    license='Simplified BSD License',
    author='Will Kahn-Greene',
    author_email='willkg@bluesock.org',
    keywords='py.test pytest',
    url='https://github.com/willkg/pytest-wholepath',
    zip_safe=True,
    py_modules=['pytest_wholepath'],
    entry_points={
        'pytest11': [
            'wholepath = pytest_wholepath'
        ]
    },
    install_requires=[
        'pytest>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
