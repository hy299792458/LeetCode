class Solution(object):
    def flipLights(self, n, m):
        m1 = 0
        m2 = 0
        m3 = 0
        m4 = 0
        for i in range(n):
            m1 *= 2
            m2 *= 2
            m3 *= 2
            m4 *= 2
            m1 += i % 2
            m2 += (i + 1) % 2
            if i % 3 == 0:
                m3 += 1
            m4 += 1
        #print m1, m2, m3, m4
        temp = set([m4])
        for _ in range(m):
            newTemp = set()
            for l in temp:
                newTemp.add(l ^ m1 & m4)
                newTemp.add(l ^ m2 & m4)
                newTemp.add(l ^ m3 & m4)
                newTemp.add(l ^ m4 & m4)
            temp = newTemp
        #print list(temp)
        return len(temp)
