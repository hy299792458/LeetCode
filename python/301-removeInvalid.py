class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return [""]
        n = len(s)
        def removeRec(s, start_check, start_remove, leftPar, rightPar):
            left = 0
            for i in xrange(start_check, len(s)):
                if s[i] == leftPar: left += 1
                if s[i] == rightPar: 
                    left -= 1
                    if left < 0: 
                        var = []
                        for j in xrange(start_remove, i+1):
                            if s[j] == rightPar and (j == start_remove or s[j-1] != rightPar): 
                                var += removeRec(s[:j]+s[j+1:], i, j, leftPar, rightPar)
                        return var
            if left == 0: return [s]
            return [x[::-1] for x in removeRec(s[::-1], 0, 0, rightPar, leftPar)]
        
        return removeRec(s, 0, 0, '(', ')')
