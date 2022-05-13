#!/usr/bin/env python
from __future__ import with_statement  # Python 2.5

import os
import sys
import unittest

import pycksum


class PyCksumTests(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "fixtures/test1.txt")

    def test_string(self):
        self.assertEqual(pycksum.cksum(""), 4294967295)  # echo -n | cksum
        self.assertEqual(
            pycksum.cksum("Hello world\n"), 3083891038
        )  # echo "Hello world" | cksum

    def test_file(self):
        with open(self.file_path) as fd:
            self.assertEqual(pycksum.cksum(fd), 3083891038)

    def test_iterable(self):
        test_list = ["Hello", " ", "world", "\n"]
        self.assertEqual(pycksum.cksum(test_list), 3083891038)

    def test_incremental(self):
        c = pycksum.Cksum()
        fd = open(self.file_path)
        while 1:
            data = fd.read(1)
            if len(data) == 0:
                break
            c.add(data)
        fd.close()
        self.assertEqual(c.get_cksum(), 3083891038)

    def test_bytes(self):
        if sys.version_info < (3,):
            b = b'"Seen On a Bumper Sticker: I\'d give my right hand to be ambidextrous."'
            self.assertEqual(pycksum.cksum(b), 21159027)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
