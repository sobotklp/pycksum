from distutils.core import setup
from distutils.extension import Extension

from pycksum import version

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
    ],

setup(
    name = "cksum",
    description = "Python implementation of Unix checksum algorithm",
    version = version,
    author = 'Lewis Sobotkiewicz',
    author_email = 'lewis.sobot@gmail.com',
    cmdclass = cmdclass,
    ext_modules = ext_modules,
)
