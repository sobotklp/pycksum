from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

cmdclass = {"build_ext": build_ext}
ext_modules = [
    Extension("_pycksum", ["ext/_pycksum.pyx"]),
]

setup(
    name="pycksum",
    description="Python implementation of Unix checksum algorithm",
    packages=["pycksum"],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
)
