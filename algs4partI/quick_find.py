#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

'''
Give the id[] array that results from the following sequence of 6 union
operations on a set of 10 items using the quick-find algorithm.

    8-1 5-8 2-7 2-4 5-0 3-9 

Recall: our quick-find convention for the union operation p-q is to change id[p]
(and perhaps some other entries) but not id[q].
'''

import sys


def union(p, q):
    value_p = nodes[p]
    for i in xrange(10):
        if nodes[i] == value_p:
            nodes[i] = nodes[q]	


if __name__ == '__main__':

    nodes = range(10)
    print 'init', nodes

    if len(sys.argv) > 1:
        for action in sys.argv[1:]:
            p, q = action.split('-')
            union(int(p), int(q))
            print 'union %s-%s' %(p, q), nodes

    print 'finished', nodes
