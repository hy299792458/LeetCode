class Solution(object):
    def findWords(self, words):
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        l = [l1, l2, l3]
        def check(word):
            temp = word.lower()
            pos = 0
            for i in range(3):
                if temp[0] in l[i]:
                    pos = i
            return all(s in l[pos] for s in temp)
        return filter(check, words)
