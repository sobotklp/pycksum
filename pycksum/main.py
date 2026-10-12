import sys
from contextlib import nullcontext

import pycksum


def main():
    fnames = sys.argv[1:] if len(sys.argv) > 1 else [None]

    for fname in fnames:
        with nullcontext(sys.stdin) if fname is None else open(fname, "rb") as fd:
            c = pycksum.Cksum()
            while 1:
                data = fd.read(4096)
                if len(data) == 0:
                    break
                c.add(data)

        print(f"{c.get_cksum()} {c.get_size()} {fname or ''}")


if __name__ == "__main__":
    main()
