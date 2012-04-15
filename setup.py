from setuptools import setup
from setuptools.extension import Extension
from pycksum import version

long_description = open('README', 'rb').read()

setup(
    name = "pycksum",
    description = "Python implementation of Unix checksum algorithm",
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
    }
)
