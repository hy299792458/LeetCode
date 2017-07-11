class Solution(object):
    def numberOfBoomerangs(self, points):
        re = 0
        for i in range(len(points)):
            dis = {}
            for j in range(len(points)):
                if i == j:
                    continue
                p1 = points[i]
                p2 = points[j]
                d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                dis[d] = dis.get(d, 0) + 1
            for num in dis.values():
                re += (num - 1) * num / 2
        return re * 2
