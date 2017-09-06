class Solution(object):
    def findRestaurant(self, list1, list2):
        dict1 = {}
        dict2 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        for i in range(len(list2)):
            dict2[list2[i]] = i
        re = []
        tol = float('inf')
        for rest in list1:
            if rest in dict2:
                total = dict1[rest] + dict2[rest]
                if total < tol:
                    re = [rest]
                    tol = total
                elif total == tol:
                    re.append(rest)
        return re
