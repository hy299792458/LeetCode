class Solution(object):
    def isRectangleCover(self, rectangles):
        corner = {}
        area = 0
        bound = rectangles[0]
        for rec in rectangles:
            d, l, u, r = rec
            bound = [min(d, bound[0]), min(l, bound[1]), max(u, bound[2]), max(r, bound[3])]
            area += (u - d) * (r - l)
            corner[(l, u)] = corner.get((l, u), 0) + 1
            corner[(r, u)] = corner.get((r, u), 0) + 1
            corner[(l, d)] = corner.get((l, d), 0) + 1
            corner[(r, d)] = corner.get((r, d), 0) + 1
        d, l, u, r = bound
        if area != (u - d) * (r - l):
            return False
        boundCorner = [(k, corner[k]) for k in corner if corner[k] not in (2,4)]
        if len(boundCorner) != 4:
            return False
        for temp in [((l, u), 1), ((r, u), 1), ((l, d), 1), ((r, d), 1)]:
            if temp not in boundCorner:
                return False
        return True
