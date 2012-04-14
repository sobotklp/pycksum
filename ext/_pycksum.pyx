"""
This module implements a Cython-compatible C extension for computing cksums 
"""

cdef extern from "_pycksum.h":
    unsigned long *crctab

cdef inline long UNSIGNED(long n):
    return n & 0xffffffff

def _memcrc(bytes by,unsigned long s=0):
    cdef char* b = by
    cdef Py_ssize_t sz = len(by)
    cdef char ch
    cdef long tabidx

    for i in range(sz):
        ch = b[i]
        tabidx = (s>>24)^ch
        s = ((s << 8)&0xffffffff) ^ crctab[tabidx%256]
    return s, sz

