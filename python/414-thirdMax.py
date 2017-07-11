class Solution(object):
    def thirdMax(self, nums):
        order = [-float('inf')] * 3
        for num in nums:
            if num in order:
                continue
            if num > order[0]:
                order.insert(0, num)
            elif num > order[1]:
                order.insert(1, num)
            elif num > order[2]:
                order.insert(2, num)
            order = order[:3]
        return order[2] if order[2] > -float('inf') else order[0]
