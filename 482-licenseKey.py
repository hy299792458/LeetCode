class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace('-', '').upper()
        p = len(S) % K
        res = [S[:p]] if p > 0 else []
        while p + K <= len(S):
            res.append(S[p : p + K])
            p += K
        return '-'.join(res)
