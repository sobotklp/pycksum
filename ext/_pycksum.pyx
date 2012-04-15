"""
This module implements a Cython-compatible C extension for computing cksums 
"""
from libc.stdint cimport uint32_t

cdef extern from "_pycksum.h":
    uint32_t _memcksum(char *b, uint32_t s, Py_ssize_t sz)

def _memcrc(bytes by,uint32_t s=0):
    cdef char* b = by
    cdef Py_ssize_t sz = len(by)
    return _memcksum(b, s, sz), sz

