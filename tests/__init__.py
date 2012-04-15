#!/usr/bin/env python
import os,unittest

import pycksum

class PyCksumTests(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "fixtures/test1.txt")

    def test_string(self):
        self.assertEquals(pycksum.cksum(""), 4294967295L) # echo -n | cksum
        self.assertEquals(pycksum.cksum("Hello world\n"), 3083891038L) # echo "Hello world" | cksum

    def test_file(self):
        self.assertEquals(pycksum.cksum(open(self.file_path)), 3083891038L)

    def test_iterable(self):
        l = ["Hello", " ", "world", "\n"]
        self.assertEquals(pycksum.cksum(l), 3083891038L)

    def test_incremental(self):
        c = pycksum.Cksum()
        fd = open(self.file_path)
        while 1:
            data = fd.read(1)
            if len(data) == 0:
                break
            c.add(data)
        fd.close()
        self.assertEquals(c.get_cksum(), 3083891038L)

def main():
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()
