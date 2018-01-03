# -*- coding: utf-8 -*-
# @Date:   2017-12-20 22:15:57
# @Last Modified time: 2017-12-20 22:16:03


def straight(l):
    for i in range(1, len(l)):
        for j in range(i)[::-1]:
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            else:
                break
    return l


def bubble(l):
    for i in range(len(l))[::-1]:
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


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
        if low - 1 > left:
            quick(l, left, low - 1)
        if low + 1 < right:
            quick(l, low + 1, right)
    return l


print(straight([2, 56, 6, 10, 3, 56, 9, 12]))
print(bubble([2, 56, 6, 10, 3, 56, 9, 12]))
print(quick([2, 56, 6, 10, 3, 56, 9, 12]))