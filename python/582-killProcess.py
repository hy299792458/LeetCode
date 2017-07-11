class Solution(object):
    def killProcess(self, pid, ppid, kill):
        killed = set([kill])
        alive = set([0])
        parents = {}
        for c, p in zip(pid, ppid):
            parents[c] = p
        for p in pid:
            path = []
            while p not in killed and p not in alive:
                path.append(p)
                p = parents[p]
            if p in killed:
                for node in path:
                    killed.add(node)
            else:
                for node in path:
                    alive.add(node)
        return list(killed)
