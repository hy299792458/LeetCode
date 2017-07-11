class Solution(object):
    def findCircleNum(self, M):
        cir = 0
        seen = set()
        def DFS(i):
            for j in range(len(M)):
                if M[i][j] == 1 and j not in seen:
                    seen.add(j)
                    DFS(j)
        for i in range(len(M)):
            if i not in seen:
                seen.add(i)
                DFS(i)
                cir += 1
        return cir
