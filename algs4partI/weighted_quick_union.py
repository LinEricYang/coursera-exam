#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

'''
Give the id[] array that results from the following sequence of 9 union
operations on a set of 10 items using the weighted quick-union algorithm from
lecture.

    2-6 6-5 8-4 0-7 2-3 8-7 6-1 2-4 0-9 

Recall: when joining two trees of equal size, our weighted quick union
convention is to make the root of the second tree point to the root of the
first tree. Also, our weighted quick union algorithm uses union by size (number
of nodes), not union by height.
'''

import sys


def root(index):
    while index != nodes[index]:
        index = nodes[index]
    return index


def union(p, q):
    root_p = root(p)
    root_q = root(q)
    if size[root_p] >= size[root_q]:
        nodes[root_q] = root_p
        size[root_p] += size[root_q]
    else:
        nodes[root_p] = root_q
        size[root_q] += size[root_p]


if __name__ == '__main__':

    nodes = range(10)
    size = [1 for i in xrange(10)]
    print 'init', nodes
    print 'size', size

    if len(sys.argv) > 1:
        for action in sys.argv[1:]:
            p, q = action.split('-')
            union(int(p), int(q))
            print 'union %s-%s' %(p, q)
            print nodes
            print size, '\n'

    print 'finished', nodes
    print 'size', size
