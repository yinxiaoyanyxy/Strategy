import os
import sys


class FooClass(object):
    def __init__(self):
        print('my first object')

    def read_in(self, filename):
        f_out = open(filename, 'r')
        lines = f_out.readlines()
        for line in lines:
            print(line.strip())

    def playtime(self):
        print(sys.platform)


if __name__ == '__main__':
    fooclass = FooClass()
    # fooclass.read_in('/Users/yinxiaoyan/Documents/_read_me.txt')
    fooclass.playtime()

import os
