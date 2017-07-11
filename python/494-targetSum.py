class Solution(object):
    def findTargetSumWays(self, nums, S):
        store = {0 : 1}
        for num in nums:
            if num == 0:
                for k in store:
                    store[k] *= 2
            else:
                newStore = {}
                for k in store:
                    add = k + num
                    sub = k - num
                    newStore[add] = newStore.get(add, 0) + store[k]
                    newStore[sub] = newStore.get(sub, 0) + store[k]
                store = newStore
        return store.get(S, 0)
