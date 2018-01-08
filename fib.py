# -*- coding: utf-8 -*-
# @Date:   2016-10-24 16:47:13
# @Last Modified time: 2018-01-08 16:13:45


class Fib(object):

    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.a <= self.max:
            self.a, self.b = self.b, self.a + self.b
            return self.a
        else:
            raise StopIteration()

print[i for i in Fib(30)]
