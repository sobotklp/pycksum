
from setuptools import setup, find_packages
from setuptools.extension import Extension

from pycksum import version

long_description = open('README', 'rb').read()

try:
    from Cython.Distutils import build_ext
    cmdclass = {'build_ext': build_ext}
    ext_modules = [
    	Extension("_pycksum", ["ext/_pycksum.pyx"])
    ]
except ImportError:
    cmdclass = {}
    ext_modules = [
    	Extension("_pycksum", ["ext/_pycksum.c"])
    ]

setup(
    name = "pycksum",
    description = "Python implementation of Unix checksum algorithm",
    long_description = long_description,
    packages=find_packages(),
    url = "https://github.com/sobotklp/pycksum",
    version = version,
    author = 'Lewis Sobotkiewicz',
    author_email = 'lewis.sobot@gmail.com',
    cmdclass = cmdclass,
    ext_modules = ext_modules,
    entry_points = {
        'console_scripts' : [
            'pycksum = pycksum.main:main',
        ]
    }
)
