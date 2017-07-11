class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        ls = len(s)
        def dfs(pos, ip):
            if len(ip) == 4:
                if pos == ls:
                    res.append('.'.join(ip))
            else:
                for tail in range(pos + 1, min(ls + 1, pos + 4)):
                    temp = s[pos:tail]
                    if str(int(temp)) == temp and 0 <= int(temp) < 256:
                        dfs(tail, ip + [temp])
        dfs(0, [])
        return res
