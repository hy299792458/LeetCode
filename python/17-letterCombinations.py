class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': \
        'jkl', '6': 'mno','7':'pqrs', '8': 'tuv', '9': 'wxyz'}
        temp = ['']
        for num in digits:
            newTemp = []
            for choice in chars[num]:
                for l in temp:
                    newTemp.append(l + choice)
            temp = newTemp
        return temp
