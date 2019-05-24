#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    # arr = list(input()).reverse()
    # print(arr)
    # arr1 = list(map(int, input()))
    # print(arr1)
    # arr2 = list(map(int, input().rstrip()))
    # print(arr2)
    # arr3 = list(map(int, input().rstrip().split()))
    # print(arr3)
    # print(arr3.reverse())
    # print(arr[::-1])
    a = list(map(int, input().rstrip().split()[::-1]))
    b = ''
    for i in a:
        b += str(i) + ' '
    print(b)