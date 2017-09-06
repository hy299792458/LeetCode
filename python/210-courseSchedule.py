class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        pre = [set() for _ in range(numCourses)]
        nex = [set() for _ in range(numCourses)]
        for t, p in prerequisites:
            pre[t].add(p)
            nex[p].add(t)
        
        res = []
        taken = set()
        def dfs(i):
            for c in nex[i]:
                pre[c].remove(i)
                if len(pre[c]) == 0 and c not in taken:
                    taken.add(c)
                    res.append(c)
                    dfs(c)
            nex[i] = set()
        for i in range(numCourses):
            if len(pre[i]) == 0 and i not in taken:
                taken.add(i)
                res.append(i)
                dfs(i)
        return res if len(res) == numCourses else []
