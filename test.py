import sys, cksum

def main():
    fname = sys.argv[-1]
    fd = open(fname, "rb")

    c = cksum.Cksum()
    _sz = 0
    while 1:
        data = fd.read(4096)
	if len(data) == 0:
	    break
	c.add(data)
	_sz += len(data)
    print "%d\t%d\t%s" %  (c.get_cksum(), _sz, fname)

if __name__ == "__main__":
    main()
