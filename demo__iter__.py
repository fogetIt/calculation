# -*- coding: utf-8 -*-
# @Date:   2016-10-24 16:47:13
# @Last Modified time: 2018-01-05 12:11:21


class Fib(object):

    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.a <= self.max:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            return x
        else:
            raise StopIteration()

for i in Fib(30):
    print i,
