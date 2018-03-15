#Homework 3 - Jake Hayes
#Nov. 21, 2016

import sys
import random
import time
sys.path.append('/Users/Jake/Documents/Senior Year 2/Geog5222/')

from geom.point import *
from indexing.bst import *
from indexing.kdtree1 import *
from indexing.kdtree3 import *
from indexing.pointquadtree1 import *
from interpolation.idw import *
from interpolation.prepare_interpolation_data import *

#Question 1
fname = '/Users/Jake/Documents/Senior Year 2/Geog5222/data/necoldem.dat'
f = open(fname, 'r')
Z = f.readlines()
Z = [x.strip().split() for x in Z]
Z = [ [ float(x[0]),float(x[1]),float(x[2])] for x in Z]
points = [Point(x[0], x[1], x[2]) for x in Z]
x = Point(337000, 4440911)
N = 10
kd_tree = kdtree2(points)
Z1 = prepare_interpolation_data(x, Z, N)[0]
Z2 = kdtree_nearest_neighbor_query(kd_tree, x, N)

Z2 = [ (z[0].x, z[0].y, z[0].key, z[1]) for z in Z2]
#print Z1

time1 = time.time()
# computation starts here
IDW(Z1, 0)
# computation done
time2 = time.time()
IDW(Z2, 0)
time3 = time.time()
print 'the first method takes',
print("%.7f" % float(time2-time1)),
print 'seconds'
print 'the second method takes',
print("%.7f" % float(time3-time2)),
print 'seconds'

#Question 2
x = points[0]
Z3 = kdtree_nearest_neighbor_query(kd_tree, x, N)
Z3 = [ (z[0].x, z[0].y, z[0].key, z[1]) for z in Z3 if z[0] != x]
print "The known value is", x.key
print "The estimated value is", IDW(Z3, 0)
print "As you can see these are not equal"

#Question 3
points = [Point(random.randint(0, 100), random.randint(0, 100)) for i in range(10)]
tt = bt(points)
#bt_print(tt)
#print
#tree_print(tt)
"""
    This is correct because it goes from the leftmost branch and then has
    the right branch after it goes through the root. This is the correct
    order when working through the binary search tree.
"""

#Question 4
def leftTree(points):
    root = kDTreeNode(point=points[0], left=None, right=None)
    for p in points[1:]:
        node = kDTreeNode(point=p, left=None, right=None)
        p0, lr = query_kdtree(root, p, 0, False)
        p0.left = node
    return root 

#Question 5
def insert_setree(q, p):
    n = search_pqtree(q, p, False)
    node = PQuadTreeNode(point=p)
    n.se = node
    
def SETree(points):
    root = PQuadTreeNode(point = data[0])
    for p in data[1:]:
        insert_setree(root, p)
    return root

#Function Calls. To make it easier to turn off everything.
#Question 4
test_points = [Point(random.randint(0, 100), random.randint(0, 100)) for i in range(10)]
test_tree = leftTree(test_points)
#print("Printing test tree")
#tree_print(test_tree)

#Question 5
test_points5 = [Point(random.randint(0, 100), random.randint(0, 100)) for i in range(10)]
test_tree5 = leftTree(test_points)
#print("Printing test tree 5")
#tree_print(test_tree5)
