from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

version_info = [0,9,0]
version = ".".join(map(str, version_info))

setup(
    name = "Python implementation of Unix checksum algorithm",
    version = version,
    author = 'Lewis Sobotkiewicz',
    author_email = 'lewis.sobot@gmail.com',

    cmdclass = {'build_ext': build_ext},
    ext_modules = [
    	Extension("_cksum", ["ext/_cksum.pyx"])
    ],
)
