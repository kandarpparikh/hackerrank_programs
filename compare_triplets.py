#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    acount = 0
    bcount =0
    farray = []
    for i in range(len(a)):
        if a[i] > b[i]:
            acount = acount + 1
        elif a[i] < b[i]:
            bcount = bcount + 1
        else:
            continue
    farray.append(acount)
    farray.append(bcount)
    return farray


if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
