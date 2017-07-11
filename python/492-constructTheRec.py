class Solution(object):
    def constructRectangle(self, area):
        W = int(math.sqrt(area))
        while True:
            if area % W == 0:
                return (area / W, W)
            W -= 1
