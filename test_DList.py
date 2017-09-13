#!/usr/bin/env python

#----------------------------------------------------------------------
# test_DList.py
# Gavyn Partlow, Andrew Harmon
# 9/12/17
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

    def test_len(self):
        a = DList()
        self.assertEqual(a.__len__(), 0)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a.__len__(), 5)
        b = DList()
        self.assertEqual(b.__len__(), 0)

    def test_find(self):
        a = DList()
        self.assertRaises(IndexError, a._find, 3)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a._find(2).item, 3)
        self.assertEqual(a._find(-2).item, 6)

    def test_getItem(self):
        a = DList()
        self.assertRaises(IndexError, a.__getitem__, 2)
        a.append(7)
        self.assertRaises(IndexError, a.__getitem__, 2)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a.__getitem__(2), 3)
        self.assertEqual(a.__getitem__(3), 6)

    def test_setItem(self):
        a = DList()
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        a.__setitem__(1, 4)
        self.assertEqual(a.__getitem__(1), 4)
        a.__setitem__(0, 6)
        self.assertEqual(a.__getitem__(0), 6)

    def test_delItem(self):
        a = DList()
        a.__delitem__(0)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        a.__delitem__(0)
        a.__delitem__(0)
        a.__delitem__(0)
        a.__delitem__(0)
        a.__delitem__(0)
        self.assertEqual(a.__len__(), 0)

    def test_append(self):
        a = DList()
        a.append(1)
        self.assertEqual(a.__len__(), 1)
        self.assertEqual(a.__getitem__(0), 1)
        a.append(3)
        self.assertEqual(a.__len__(), 2)
        self.assertEqual(a.__getitem__(1), 3)

    def test_insert(self):
        a = DList()
        a.insert(3, 7)
        self.assertEqual(a.__len__(), 1)
        self.assertEqual(a.__getitem__(0), 7)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        a.insert(2, 4)
        a.insert(2, 7)
        self.assertEqual(a.__getitem__(3), 4)
        self.assertEqual(a.__getitem__(6), 6)

    def test_min(self):
        a = DList()
        self.assertRaises(ValueError, a.__min__)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a.__min__(), 3)

    def test_max(self):
        a = DList()
        self.assertRaises(ValueError, a.__max__)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a.__max__(), 9)

    def test_extend(self):
        checkListOne = [ ]
        checkListTwo = [1, 3, 5, 7, 9, 8, 6, 4, 2]
        a = DList()
        a.extend(checkListOne)
        self.assertEqual(a.__len__(), 0)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        a.extend(checkListTwo)
        self.assertEqual(a.count(1), 1)
        self.assertEqual(a.count(9), 2)
        self.assertEqual(a.count(6), 2)
        self.assertEqual(a.__len__(), 14)

    def test_count(self):
        a = DList()
        self.assertEqual(a.count(5), 0)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        a.append(7)
        a.append(3)
        a.append(9)
        a.append(9)
        a.append(7)
        self.assertEqual(a.count(3), 2)
        self.assertEqual(a.count(5), 1)
        self.assertEqual(a.count(6), 1)
        self.assertEqual(a.count(7), 3)
        self.assertEqual(a.count(9), 3)

    def test_index(self):
        a = DList()
        self.assertEqual(a.index(5), None)
        a.append(7)
        a.append(9)
        a.append(3)
        a.append(6)
        a.append(5)
        self.assertEqual(a.index(7), 0)
        self.assertEqual(a.index(9), 1)
        self.assertEqual(a.index(3), 2)
        self.assertEqual(a.index(6), 3)
        self.assertEqual(a.index(5), 4)

#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
