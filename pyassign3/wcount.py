#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Fan Hanyun"
__pkuid__  = "1700017838"
__email__  = "501180426@pku.edu.cn"
"""

import string
import sys
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    dic = {}
    for i in lines:
        if i in string.punctuation:
            lines = lines.replace(i," ")
    lines = lines.lower()
    lst = lines.split()
    newlst = list(set(lst))
    numlst = []
    for i in range(len(newlst)):
        num = lst.count(newlst[i])
        dic[newlst[i]] = num
    for (a,b) in dic.items():
        numlst += [(b,a)]
    numlst.sort(reverse = True)
    for i in range(topn):
        print(numlst[i][1].ljust(15)+str(numlst[i][0]))
if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
