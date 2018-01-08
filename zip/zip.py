# -*- coding: utf-8 -*-
# @Date:   2017-12-28 18:48:46
# @Last Modified time: 2018-01-08 16:09:42


def zip(data):
    num = 1
    result = ''
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            num += 1
        else:
            result += data[i - 1]
            result += str(num)
            num = 1
        if i == len(data) - 1:
            result += data[i]
            result += str(num)
    return result


def unzip(data):
    result = ''
    for i in range(len(data)):
        if i % 2:
            result += data[i - 1] * int(data[i])
    return result


def better_zip(data):
    num = 1
    result = ""
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            num += 1
        else:
            result += data[i - 1]
            if num > 1:
                result += str(num)
            num = 1
        if i == len(data) - 1:
            result += data[i]
            if num > 1:
                result += str(num)
    return result


print(zip('aabaaccdfffgtjki'))
print(unzip('a2b1a2c2d1f3g1t1j1k1i2'))
print(better_zip('aabaaccdfffgtjkii'))
