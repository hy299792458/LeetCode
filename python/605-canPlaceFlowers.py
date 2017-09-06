class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        count = 0
        plant = 0
        for pos in flowerbed:
            if pos == 0:
                count += 1
            elif count > 0:
                plant += (count - 1) / 2
                count = 0
        if count > 0:
            plant += (count - 1) /2
        return plant >= n
