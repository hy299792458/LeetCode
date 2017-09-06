class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for m in moves:
            if m == "U":
                x += 1
            elif m == "D":
                x -= 1
            elif m == "L":
                y += 1
            elif m == "R":
                y -= 1
        return x == 0 and y == 0
        
