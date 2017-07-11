class Solution(object):
    def leastBricks(self, wall):
        edge = {0: 0}
        for l in wall:
            temp = 0
            for brick in l[:-1]:
                temp += brick
                edge[temp] = edge.get(temp, 0) + 1
        return len(wall) - max(edge.values())
