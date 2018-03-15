import math
from point import *

from polygon_error import PolygonError

def pip_cross(point, pgon):
    """
    Determines whether a point is in a polygon. Code adopted
    from the C program in Graphics Gems IV by Haines (1994).

    Input
      pgon:   a list of points as the vertices for a polygon
              The polygon needs to be closed. Otherwise an error is raised.
      point:  the point

    Ouput
      Returns a boolean value of True or False and the number
      of times the half line crosses the polygon boundary

    History
       October 2016.
            Removed function pip_cross0
            Changed <> to !=
            Raise error if polygon is not closed (previous version modifies data)
                This requires polygon_error.py.
            Changed some variable names for better read

       October 2015. A bug in previous code, pip_cross0, is fixed.
    """
    # tx, ty = point.x, point.y
    x, y = point.x, point.y
    if pgon[0] != pgon[-1]:
        raise PolygonError('Polygon not closed')
    N = len(pgon)
    crossing_count = 0
    is_point_inside = False
    for i in range(N-1):
        p1, p2 = pgon[i], pgon[i+1]           # two consecutive points
        yside1 = (p1.y >= y)                  # p1 on/above point
        yside2 = (p2.y >= y)                  # p2 on/above point
        if yside1 != yside2:                  # p1 & p2 on two sides of half line
            xside1 = (p1.x >= x)              # p1 on/right to point
            xside2 = (p2.x >= x)              # p2 on/right to point
            if xside1 == xside2:              # p1 & p2 on same left/right side of point
                if xside1:                    # p1-p2 on the right side, intersect
                    crossing_count += 1
                    is_point_inside = not is_point_inside
            else:                             # compute intersection
                m = p2.x - (p2.y-y)*(p1.x-p2.x)/float(p1.y-p2.y)
                if m >= x:                    # p1-p2 cross half line, intersect
                    crossing_count += 1
                    is_point_inside = not is_point_inside
    return is_point_inside, crossing_count

if __name__ == "__main__":
    points = [ [0,10], [5,0], [10,10], [15,0], [20,10],
               [25,0], [30,20], [40,20], [45,0], [50,50],
               [40,40], [30,50], [25,20], [20,50], [15,10],
               [10,50], [8, 8], [4,50], [0,10] ]
    ppgon = [Point(p[0], p[1]) for p in points ]
    pts = [Point(10, 30), Point(10, 20),
           Point(20, 40), Point(5, 40)]
    for p in pts:
        result = pip_cross(p, ppgon)
        if result[0] == True:
            print "Point", p, "is IN"
        else:
            print "Point", p, "is OUT"

    points = [ [0,10], [5,0], [10,10], [15,0], [20,10] ]
    ppgon = [Point(p[0], p[1]) for p in points ]
    try:
        x = pip_cross(Point(10, 30), ppgon)
    except PolygonError as err:
        print err.message
    else:
        print x[0]
