class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        total = (C - A) * (D - B) + (G - E) * (H - F)
        l = max(A, E)
        d = max(B, F)
        u = min(D, H)
        r = min(C, G)
        if l <= r and d <= u:
            total -= (u - d) * (r - l)
        return total
