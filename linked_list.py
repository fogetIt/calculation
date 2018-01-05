# -*- coding: utf-8 -*-
# @Date:   2018-01-04 11:18:16
# @Last Modified time: 2018-01-05 13:29:48
"""
链表(linked list)是由一组被称为节点的数据元素组成的数据结构
    节点：
        信息域：结点本身的信息
        指针域：下一个结点地址的指针
    由于每个结点都包含了可以链接起来的地址信息，所以用一个变量就能够访问整个结点序列
    头节点：
        链表中的第一个节点，一般不存放数据，在一个单独的节点中存储地址
        头结点后面的第一个节点，是第一个有效节点
    尾节点：
        链表中的最后一个节点，没有后继元素，其指针域为空
    链表中的元素在内存中不是顺序存储的，而是通过存在元素中的指针联系到一起
    如果要访问链表中一个元素，需要从```第一个```元素开始，一直找到需要的元素位置
    增加和删除一个元素对于链表数据结构非常简单，只要修改元素中的指针就可以了

数组/list
    将元素在内存中连续存放
    由于每个元素占用内存相同，可以通过下标迅速访问数组中任何元素
    增加一个元素
        需要移动大量元素，在内存中空出一个元素的空间，然后将要增加的元素放在其中
    删除一个元素
        需要移动大量元素去填掉被移动的元素

如果应用需要快速访问数据，很少或不插入和删除元素，就应该用数组
如果应用需要经常插入和删除元素，就需要用链表数据结构


双向链表
    有2个指针
        一个指向前一个节点（第一个节点，指向空值或空列表）
        另一个指向后一个节点（最后一个节点，指向是空值或空列表）
循环链表
    首节点和末节点被连接在一起
    循环链表中第一个节点之前就是最后一个节点，反之亦然
"""


class Node(object):

    def __init__(self, data=None, then=None):
        self.data = data
        self.then = then


class Chain(object):

    def __init__(self, *seq):
        """
        从后向前生成节点
        """
        self.length = len(seq)
        self.tail = Node(data=seq[-1]) if seq else Node()
        temp = self.tail
        for i in range(len(seq) - 1)[::-1]:
            node = Node(data=seq[i], then=temp)
            temp = node
        self.head = Node(then=temp) if temp else Node()

    @property
    def is_empty(self):
        return False if self.length else True

    def append(self, val):
        if self.is_empty:
            self.__init__(val)
        else:
            tail = Node(data=val)
            self.tail.then = tail
            self.tail = tail
            self.length += 1

    def clear(self):
        self.length = 0
        self.head = self.tail = Node()

    def __iter__(self):
        self.i = 0
        # 返回实例本身，作为迭代对象
        return self

    def next(self):
        error_text = self.__check_index(self.i)
        if error_text:
            raise StopIteration()
        else:
            data = self.__get_node(self.i).data
            self.i += 1
            return data

    def __get_node(self, i):
        node = self.head
        while i >= 0:
            node = node.then
            i -= 1
        return node

    def __check_index(self, i):
        if self.is_empty:
            return "chain is empty"
        elif not 0 <= i < self.length:
            return "index out of range"
        return None

    def __getitem__(self, i):
        error_text = self.__check_index(i)
        if error_text:
            return error_text
        else:
            return self.__get_node(i).data

    def delete(self, i):
        error_text = self.__check_index(i)
        if error_text:
            return error_text
        elif self.length == 1:
            self.clear()
        else:
            if i == 0:
                prev = self.head
            else:
                prev = self.__get_node(i - 1)
            prev.then = self.__get_node(i + 1)
            self.length -= 1

    def insert(self, i, val):
        error_text = self.__check_index(i)
        if error_text:
            return error_text


c = Chain(5, 3, 7, 0)
print c[1]
for i in c:
    print i,
c.delete(2)
print
for i in c:
    print i,
