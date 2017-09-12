#!/usr/bin/env python

#----------------------------------------------------------------------
# test_DList.py
# Gavyn Partlow
# 09/06/2017
#----------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '..')
from DList import *

#----------------------------------------------------------------------

class DListTest(unittest.TestCase):

    #------------------------------------------------------------------

    def check_list(self, linked, lst):

        a = list(linked)
        b = lst[:]
        self.assertEqual(a, b)
        a = list(linked.reverse_iter())
        b.reverse()
        self.assertEqual(a, b)
        
    #------------------------------------------------------------------

    def test_init(self):

        a = DList()
        self.assertEqual(len(a), 0)
        a = DList([1, 2, 3, 4])
        self.assertEqual(len(a), 4)
        self.check_list(a, [1, 2, 3, 4])

    #------------------------------------------------------------------

    def test_pop(self):

        a = DList()
        for i in range(10):
            a.append(i)
        b = list(range(10))
        self.check_list(a, b)

        self.assertEqual(a.pop(), 9)
        a.append(9)

        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)
        
        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(5), b.pop(5))
        self.check_list(a, b)
        
        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)
        
        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(1), b.pop(1))
        self.check_list(a, b)

        self.assertEqual(a.pop(1), b.pop(1))
        self.check_list(a, b)

        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)

        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

    #------------------------------------------------------------------

    def test_remove(self):

        a = DList()
        b = []
        for i in range(10):
            a.append(i)
            b.append(i)
            
        a.remove(0)
        a.remove(5)
        a.remove(9)

        b.remove(0)
        b.remove(5)
        b.remove(9)
        
        self.assertEqual(len(a), len(b))
        self.check_list(a, b)

        self.assertRaises(ValueError, a.remove, 10)

#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
