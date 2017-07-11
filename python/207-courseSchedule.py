class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        count = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for cou, pre in prerequisites:
            adj[pre].append(cou)
            count[cou] += 1
        visited = set()
        def dfs(cou):
            if cou in visited:
                return 
            else:
                visited.add(cou)
            for course in adj[cou]:
                count[course] -= 1
                if count[course] == 0:
                    dfs(course)
            #print count
        for i in range(numCourses):
            if count[i] == 0:
                dfs(i)
        return sum(count) == 0
