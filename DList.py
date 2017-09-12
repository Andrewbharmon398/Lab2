#!/usr/bin/env python

#----------------------------------------------------------------------
# DList.py
# Gavyn Partlow
# 09/05/2017
#----------------------------------------------------------------------

import sys

from DListNode import *

#----------------------------------------------------------------------

class DList:

    '''implementation of subset of Python built-in list API using
    a doubly linked list'''

    # List implemented as doubly linked nodes
    # invariant:
    # self.size indicates the number of items in the list
    # if self.size == 0, self.head is None otherwise
    # self.head is a reference to the first DListNode in list
    # self.tail is a reference to the last DListNode in the list to
    #   make the append operation efficient
    # preconditions for each method are indicated by the assert test
    
    #------------------------------------------------------------------

    def __init__(self, seq=None):

        '''creates an empty list'''

        self.size = 0
        self.head = None
        self.tail = None
        if seq:
            self.extend(seq)
    
    #------------------------------------------------------------------
    
    def __len__(self):

        '''returns number of items in the list'''

        return self.size
    
    #------------------------------------------------------------------

    def __iter__(self):

        '''forward iterator'''

        # Iterate through all nodes, returning the item in each node.
        curNode = self.head
        while curNode:
            yield curNode.item
            curNode = curNode.next
    
    #------------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list;
        for non negative positions, 0 is first item, size-1 is last item
        for negative positions, -1 is the last item -size is the first
        item'''

        # Raise error if position is out of range
        if not (self.size > position >= -self.size):
            raise IndexError('DList assignment index out of range')

        # Convert negative positions to corresponding positive position
        if position < 0:
            position = self.size + position

        # If the position is in the first half of the list, start from beginning.
        # Otherwise, start from the end.
        if self.size // 2 > position:
            curNode = self.head
            for i in range(position):
                curNode = curNode.next
        else:
            curNode = self.tail
            for i in range(self.size - position - 1):
                curNode = curNode.prev
        return curNode

    
    #------------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position'''

        # Raise error if position is out of range, since get error is different
        # than del and set errors, for some ungodly reason.
        if not (self.size > position >= -self.size):
            raise IndexError('DList index out of range')

        return self._find(position).item
    
    #------------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value'''

        self._find(position).item = value
    
    #------------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list'''

        self._delete(position)
    
    #------------------------------------------------------------------

    def _delete(self, position):

        '''private method to delete item at location position from the list'''

        # If position is not head or tail and size != 1, find previous node, delete next node, and mend links.
        # Otherwise, adjust head or tail appropriately. Adjust size.
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size - 1 == position:
            self.tail = self.tail.prev
            self.tail.next = None
        elif position == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            prevNode = self._find(position - 1)
            prevNode.next = prevNode.next.next
            prevNode.next.prev = prevNode
        self.size -= 1
    
    #------------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list'''

        # Check if list is empty, and adjust head and tail appropriately.
        # Else, set the tail.next to a new node, then update tail and size.
        if self.size == 0:
            self.head = DListNode(x)
            self.tail = self.head
        else:
            self.tail.next = DListNode(x, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1
    
    #------------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x before position i in the list'''

        # If inserting at the beginning or end, just update head or append.
        # Otherwise, find previous node, create new node, and update links and size.
        if i == 0:
            self.head.prev = DListNode(x, next=self.head)
            self.head = self.head.prev
            self.size += 1
        elif i >= self.size:
            self.append(x)
        else:
            prevNode = self._find(i - 1)
            newNode = DListNode(x, prevNode, prevNode.next)
            newNode.next.prev = newNode
            prevNode.next = newNode
            self.size += 1
    
    #------------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item'''

        # Store node at i as a returnNode, update tail and size, and then return the returnNode's item.
        if i is None:
            i = self.size - 1
        elif abs(i) - 1 >= self.size <= i:
            raise IndexError('pop index out of range')
        returnNode = self._find(i)
        self._delete(i)
        return returnNode.item
    
    #------------------------------------------------------------------

    def remove(self, x):

        '''removes the first instance of x from the list'''

        i = self.index(x)
        if i is not None:
            self._delete(i)
        else:
            raise ValueError('DList.remove(x): x not in list')
    
    #------------------------------------------------------------------

    def __min__(self):

        '''return minimum element in the list'''

        if self.size == 0:
            raise ValueError('min() arg is an empty sequence')
        curNode = self.head
        minimum = self.head.item
        while curNode:
            if curNode.item < minimum:
                minimum = curNode.item
            curNode = curNode.next
        return minimum
    
    #------------------------------------------------------------------

    def __max__(self):

        '''return maximum element in the list'''

        if self.size == 0:
            raise ValueError('max() arg is an empty sequence')
        curNode = self.head
        maximum = self.head.item
        while curNode:
            if curNode.item > maximum:
                maximum = curNode.item
            curNode = curNode.next
        return maximum
    
    #------------------------------------------------------------------

    def extend(self, l):

        '''add each element of list l onto the list'''

        # Iterate through the passed sequence, appending each item.
        for x in l:
            self.append(x)
    
    #------------------------------------------------------------------

    def count(self, x):

        '''return number of occurrences of x in the list'''

        # Initialize tally and iterate through nodes, updating tally as necessary.
        tally = 0
        for item in self:
            if item == x:
                tally += 1
        return tally

    #------------------------------------------------------------------

    def index(self, x, start=0):

        '''return position of first occurence of x in the list starting
        at position start'''

        # Initialize curNode to start position and iterate until node's item is x, then return.
        curNode = self._find(start)
        while curNode and curNode.item != x:
            curNode = curNode.next
            start += 1
        if self.size == start:
            return None
        return start
    
    #------------------------------------------------------------------

    def reverse_iter(self):

        '''iterate over items in reverse'''

        curNode = self.tail
        while curNode:
            yield curNode.item
            curNode = curNode.prev

    #------------------------------------------------------------------

    def __str__(self):

        s = '['
        for node in self:
            s += '{}, '.format(node)
        s = s[:-2]
        s += ']'
        return s
    
#----------------------------------------------------------------------
