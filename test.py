import sys, cksum

def main():
    fnames = sys.argv[1:]
    for fname in fnames:
        fd = open(fname, "rb")

        c = cksum.Cksum()
        sz = 0
        while 1:
            data = fd.read(4096)
            if len(data) == 0:
	        break
            c.add(data)
            sz += len(data)

        print "%d\t%d\t%s" %  (c.get_cksum(), sz, fname)

if __name__ == "__main__":
    main()
