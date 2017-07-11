# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        group = collections.defaultdict(list)
        for p in points:
            group[p.x].append(p)
        xaxis = sorted(group.keys())
        if len(xaxis) <= 2:
            return points
        res = group[xaxis[0]] + group[xaxis[-1]]
        up = [max(group[xaxis[0]], key = lambda x: x.y)]
        down = [min(group[xaxis[0]], key = lambda x: x.y)]
        for x in xaxis[1:]:
            c1 = max(group[x], key = lambda x: x.y)
            c2 = min(group[x], key = lambda x: x.y)
            while len(up) >= 2 and (c1.y - up[-2].y) * (up[-1].x - up[-2].x) > (up[-1].y - up[-2].y) * (c1.x - up[-2].x):
                up.pop()
            up.append(c1)
            while len(down) >= 2 and (c2.y - down[-2].y) * (down[-1].x - down[-2].x) < (down[-1].y - down[-2].y) * (c2.x - down[-2].x):
                down.pop()
            down.append(c2)
            #print map(lambda x: [x.x, x.y], up)
            #print map(lambda x: [x.x, x.y], down)
        return list( set(up[1: -1] + down[1: -1] + res))
