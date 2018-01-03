# -*- coding: utf-8 -*-
# @Date:   2017-12-19 20:20:11
# @Last Modified time: 2017-12-19 20:53:30
import time
from decimal import Decimal


def straight(l):
    start = Decimal(time.time())
    for i in range(1, len(l)):
        for j in range(i)[::-1]:
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            else:
                break
    end = Decimal(time.time())
    return int((end - start) * 10 ** 9), l


def DLShell(l):
    start = Decimal(time.time())
    # 分组
    g = len(l) / 2
    while g > 0:
        # 获取每组的最后一个元素
        for i in range(g, len(l)):
            # 把每个组进行直接插入排序
            for j in range(i + 1)[::-g]:
                if j -g >= 0 and l[j] < l[j - g]:
                    l[j], l[j - g] = l[j - g], l[j]
        g /= 2
    end = Decimal(time.time())
    return int((end - start) * 10 ** 9), l


print(straight([2, 56, 6, 10, 3, 56, 9, 12]))
print(DLShell([2, 56, 6, 10, 3, 56, 9, 12]))
