# -*- coding: utf-8 -*-
# @Date:   2018-01-10 16:03:36
# @Last Modified time: 2018-01-10 16:18:26
"""
栈是一种特殊的列表
栈内的元素只能通过列表的一端（栈顶）访问
类比：咖啡厅内的一摞盘子。只能从最上面取盘子，盘子洗净后，也只能摞在这一摞盘子的最上面。
栈是一种后入先出（LIFO，last-in-first-out）的数据结构，任何不在栈顶的元素都无法访问。
为了得到栈底的元素，必须先拿掉上面的元素

对栈的两种主要操作是将一个元素压入栈和将一个元素弹出栈

在Python中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
"""


class Stack(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

if __name__ == '__main__':
    s = Stack()
    s.push('val')
    print s.peek()
