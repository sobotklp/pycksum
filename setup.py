from setuptools import setup
from setuptools.extension import Extension
from pycksum import version

long_description = open('README.rst', 'rb').read()

setup(
    name = "pycksum",
    description = "Python implementation of cksum algorithm",
    long_description = long_description,
    packages=['pycksum'],
    url = "https://github.com/sobotklp/pycksum",
    version = version,
    author = 'Lewis Sobotkiewicz',
    author_email = 'lewis.sobot@gmail.com',
    ext_modules = [
        Extension("_pycksum", ["ext/_pycksum.c"])
    ],
    test_suite="tests",
    entry_points = {
        'console_scripts' : [
            'pycksum = pycksum.main:main',
        ]
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],
)
