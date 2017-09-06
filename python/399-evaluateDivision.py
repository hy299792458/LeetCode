class Solution(object):
    def calcEquation(self, equations, values, queries):
        links = collections.defaultdict(dict)
        for equ, val in zip(equations, values):
            a, b = equ
            links[a][b] = 1.0 / val
            links[b][a] = val * 1.0
        def bfs(l):
            a, b = l
            if a == b:
                if len(links[a]) > 0:
                    return 1.0
                else:
                    return -1.0
            temp = [(b, 1.0)]
            seen = set([b])
            while temp:
                newTemp = []
                for k, v in temp:
                    for nk in links[k]:
                        if nk == a:
                            return v * links[k][nk]
                        if nk in seen:
                            continue
                        else:
                            seen.add(nk)
                            newTemp.append((nk, v * links[k][nk]))
                temp = newTemp
            return -1.0
        return map(bfs, queries)
            
