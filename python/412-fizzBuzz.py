class Solution(object):
    def fizzBuzz(self, n):
        def trans(num):
            re = ''
            if num % 3 and num % 5:
                re = str(num)
            else:
                if num % 3 == 0:
                    re += 'Fizz'
                if num % 5 == 0:
                    re += 'Buzz'
            return re
        return map(trans, xrange(1, n + 1))
                
