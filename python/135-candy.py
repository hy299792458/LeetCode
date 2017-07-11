class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for _ in ratings]
        for i in range(1, len(candy)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(len(candy) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i + 1] + 1, candy[i])
        #print candy
        return sum(candy)
