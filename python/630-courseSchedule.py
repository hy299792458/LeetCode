class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key = lambda x: x[1])
        taken = []
        end = 0
        for c in courses:
            end += c[0]
            heapq.heappush(taken, -c[0])
            while end > c[1]:
                end += heapq.heappop(taken)
        return len(taken)
