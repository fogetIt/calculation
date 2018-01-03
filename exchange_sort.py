# -*- coding: utf-8 -*-
# @Date:   2017-12-20 21:58:22
# @Last Modified time: 2017-12-20 21:58:25
import time
from decimal import Decimal


def max_bubble(l):
    start = Decimal(time.time())
    for i in range(len(l))[::-1]:
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    end = Decimal(time.time())
    return int((end - start) * 10 ** 9), l


def min_bubble(l):
    start = Decimal(time.time())
    for i in range(len(l)):
        for j in range(i, len(l))[::-1]:
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
    end = Decimal(time.time())
    return int((end - start) * 10 ** 9), l


def quick(l, left=0, right=None):
    right = right if right else len(l) - 1
    if left < right:
        temp = l[left]
        low = left
        high = right
        while low < high:
            while low < high and l[high] >= temp:
                high -= 1
            l[low] = l[high]
            while low < high and l[low] <= temp:
                low += 1
            l[high] = l[low]
        l[low] = temp
        if left < low - 1:
            quick(l, left, low - 1)
        if low + 1 < right:
            quick(l, low + 1, right)
    return l


print(max_bubble([2, 56, 6, 10, 3, 56, 9, 12]))
print(min_bubble([2, 56, 6, 10, 3, 56, 9, 12]))
print(quick([2, 56, 6, 10, 3, 56, 9, 12]))
