#!/usr/bin/env python
import sys, pycksum

def main():
    if len(sys.argv) > 1:
        fds = [(open(fname, "rb"), fname) for fname in sys.argv[1:]]
    else:
        fds = [(sys.stdin, "")]

    for fd, fname in fds:
        c = pycksum.Cksum()
        sz = 0
        while 1:
            data = fd.read(4096)
            if len(data) == 0:
	            break
            c.add(data)
            sz += len(data)

        print "%d %d %s" %  (c.get_cksum(), sz, fname)

if __name__ == "__main__":
    main()
