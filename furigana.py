# -*- encoding:utf-8 -*-
import sys
import fileinput
import re

__author__ = 'Linghao Zhang'


if __name__ == '__main__':
    filenames = sys.argv[1:]
    for filename in filenames:
        for line in fileinput.input(inplace=True, backup='.bak'):
            line = re.sub(r'\[(.*?)\]\{(.*?)\}', r'<ruby>\1<rp>（</rp><rt>\2</rt><rp>）</rp></ruby>', line)
            print line,
