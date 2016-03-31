# -*- encoding:utf-8 -*-
import os
import re
import sys
import shutil
import fileinput

__author__ = 'Linghao Zhang'


if __name__ == '__main__':
    for file in sys.argv[1:]:
        shutil.copyfile(file, file+'.bak')
    for line in fileinput.input(inplace=True, backup='.tmp'):
        line = re.sub(r'\[(.*?)\]\{(.*?)\}', r'<ruby>\1<rp>（</rp><rt>\2</rt><rp>）</rp></ruby>', line)
        print line,
    for file in sys.argv[1:]:
        os.remove(file+'.tmp')
