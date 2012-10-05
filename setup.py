from setuptools import setup
from setuptools.extension import Extension
from pycksum import __version__

long_description = open('README.rst').read()

setup(
    name = "pycksum",
    description = "Python implementation of cksum algorithm",
    long_description = long_description,
    packages=['pycksum'],
    url = "https://github.com/sobotklp/pycksum",
    version = __version__,
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
    use_2to3 = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
