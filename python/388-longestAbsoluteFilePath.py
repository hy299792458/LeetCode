class Solution(object):
    def lengthLongestPath(self, input):
        if "." not in input:
            return 0
        res = 0
        indents = collections.defaultdict(list)
        subs = input.split("\n")
        for sub in subs:
            l = sub.split("\t")
            temp = len(l[-1])
            ind = len(l) - 1
            indents[ind].append(temp)
            if "." in l[-1]:
                temp += ind
                while ind > 0:
                    temp += indents[ind - 1][-1]
                    ind -= 1
            res = max(res, temp )
        #print indents
        return res
