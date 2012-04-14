from pycksum import version

long_description = open('README', 'rb').read()

# Workaround for Cython's build_ext not working with setuptools
try:
    from Cython.Distutils import build_ext
    from distutils.core import setup
    from distutils.extension import Extension
    cmdclass = {'build_ext': build_ext}
    ext_modules = [
    	Extension("_pycksum", ["ext/_pycksum.pyx"]),
    ]
except ImportError:
    from setuptools import setup, find_packages
    from setuptools.extension import Extension
    cmdclass = {}
    ext_modules = [
    	Extension("_pycksum", ["ext/_pycksum.c"])
    ]

setup(
    name = "pycksum",
    description = "Python implementation of Unix checksum algorithm",
    long_description = long_description,
    packages=['pycksum'],
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
