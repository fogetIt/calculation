# -*- coding: utf-8 -*-
# @Date:   2017-12-27 13:30:05
# @Last Modified time: 2017-12-27 13:30:18


class Simple(object):
    pass


class Single(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Single.__instance is None:
            Single.__instance = 0
            # object.__new__(cls, args)
        return Single.__instance


a1 = Simple()
a2 = Simple()
print(id(a1) == id(a2))


b1 = Single()
b2 = Single()
print(id(b1) == id(b2))