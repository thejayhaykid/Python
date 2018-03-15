"""
Point k-D trees. Part 1.

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"
import sys
sys.path.append('E:\\Senior Year 2\\Geog5222-Programming')
from geom.point import *

class kDTreeNode():
    """
    Node for point k-D trees.
    """
    def __init__(self, point, left, right):
        self.point = point
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.point)

def kdcompare(r, p, depth):
    """
    Returns the branch of searching on a k-d tree
    Input
       r: root
       p: point
       depth : starting depth of search
    Output
       A value of -1 (left branch), or 1 (right)
    """
    k = len(p)
    dim = depth%k
    if p[dim] <= r.point[dim]:
        return -1
    else:
        return 1

def kdtree(points):
    """
    Creates a point k-D tree using a predefined order of points
    """
    root = kDTreeNode(point=points[0], left=None, right=None)
    for p in points[1:]:
        node = kDTreeNode(point=p, left=None, right=None)
        p0, lr = query_kdtree(root, p, 0, False)
        if lr<0:
            p0.left = node
        else:
            p0.right = node
    return root

def kdtree2(points, depth = 0):
    """
    Creates a point k-d tree using the median point to split the data
    """
    if len(points)==0:
        return
    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda points: points[axis])
    pivot = len(points)//2
    while pivot<len(points)-1 and\
          points[pivot][axis]==points[pivot+1][axis]:
        pivot += 1
    return kDTreeNode(point=points[pivot],
                      left=kdtree2(points[:pivot],
                                   depth+1),
                      right=kdtree2(points[pivot+1:],
                                    depth+1))

def query_kdtree(t, p, depth=0, is_find_only=True):
    """
    Input
      t:            a node of a point k-D tree
      p:            target point to be found in the tree
      is_find_only: True/False, specifying type of output

    Output
      the node that contans p or None if is_find_only is True, otherwise
      the node that should be the parent node of p
    """
    if t is None:
        return
    if t.point == p and is_find_only:
        return t
    lr = kdcompare(t, p, depth)
    if lr<0:
        child = t.left
    else:
        child = t.right
    if child is None:
        if not is_find_only:
            return t, lr
        else:
            return
    return query_kdtree(child, p, depth+1, is_find_only)

if __name__ == '__main__':
    data1 = [ (2,2), (0,5), (8,0), (9,8),
              (7,14), (13,12), (14,13) ]
    points = [Point(d[0], d[1]) for d in data1]
    p = points[0]
    t1 = kdtree(points)
    t2 = kdtree2(points)

    print [ query_kdtree(t1, p) for p in points ]
    print [ query_kdtree(t2, p) for p in points ]    

