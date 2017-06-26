class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        nums = s.split('e')
        def check(num):
            if num == '':
                return False
            p = 0
            point = 0
            dig = 0
            if num[0] in '+-':
                p += 1
            while p < len(num):
                if num[p] == '.':
                    if point == 0:
                        point = 1
                    else:
                        return False
                elif num[p] in '0123456789':
                    dig += 1
                else:
                    return False
                p += 1
            if not dig:
                return False
            if point:
                return 'F'
            else:
                return 'I'
        if len(nums) == 1:
            return check(nums[0]) != False
        elif len(nums) == 2:
            return check(nums[0]) and check(nums[1]) == 'I'
        return False
                    
