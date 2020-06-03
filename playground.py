#!/bin/python3

import math
import os
import random
import re
import sys

import array


class Multiset:
    array = []
    def add(self, val):
        self.array.append(val)
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        if val in self.array:
            self.array.remove(val)
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        if val in self.array:
            return True
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):

        # returns the number of elements in the multiset
        return (len(self.array))
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    print('\n'.join(map(str, result)))

