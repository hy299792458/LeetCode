class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        store = {}
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        def check(left, desire):
            if left in store:
                return store[left]
            nums = list(left)
            if nums[-1] >= desire:
                store[left] = True
                return True
            else:
                for i in range(len(nums)):
                    if not check(tuple(nums[:i] + nums[i + 1:]), desire - nums[i]):
                        store[left] = True
                        return True
            store[left] = False
            return False
        return check((i + 1 for i in range(maxChoosableInteger)), desiredTotal)
