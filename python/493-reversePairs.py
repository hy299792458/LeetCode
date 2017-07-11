class Solution(object):
    def reversePairs(self, nums):
        self.count = 0
        def mergeSort(i, j):
            if j <= i + 1:
                return
            else:
                mid = (i + j) / 2
                mergeSort(i, mid)
                mergeSort(mid, j)
                temp = []
                p1 = c1 = i
                p2 = c2 =mid
                while c1 < mid and c2 < j:
                    if nums[c1] <= 2 * nums[c2]:
                        c1 += 1
                    else:
                        c2 += 1
                        self.count += mid - c1
                while p1 < mid and p2 < j:
                    if nums[p1] < nums[p2]:
                        temp.append(nums[p1])
                        p1 += 1
                    else:
                        temp.append(nums[p2])
                        p2 += 1
                while p1 < mid:
                    temp.append(nums[p1])
                    p1 += 1
                while p2 < j:
                    temp.append(nums[p2])
                    p2 += 1
                nums[i : j] = temp[:]
        mergeSort(0, len(nums))
        return self.count
