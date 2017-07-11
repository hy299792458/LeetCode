class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        l1, l2 = len(v1), len(v2)
        return cmp(v1 + [0]*(l2 - l1), v2 + [0]*(l1 - l2))
