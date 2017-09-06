class Solution(object):
	def largestPalindrome(self,n):
		if (n == 1): return 9
		uBound = 10**n - 1
		lBound = uBound // 10
		Found = False
		firstHalf = int(uBound * uBound / (10 ** n))

		while not Found:
			secondHalf = int(str(firstHalf)[::-1])
			palindrom = firstHalf*10**n + secondHalf

			if (len(str(palindrom))%2==0):
				for i in xrange(uBound // 11,(lBound+1) // 11,-1):
					if (palindrom / (11*i) > uBound):
						break
					if ((palindrom % (11*i)) == 0):
						Found = True
						break
			else:
				for i in xrange(uBound, lBound + 1, -1):
					if (palindrom / i > uBound or i * i < palindrom):
						break
					if (palindrom % i == 0):
						Found = True
						break
			firstHalf -= 1
		return palindrom % 1337
