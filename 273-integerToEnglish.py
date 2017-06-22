class Solution(object):
    def numberToWords(self, num):
        to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def trans(n):
            #print n
            re = []
            if n / 100:
                re.append(to19[n / 100 ])
                re.append('Hundred')
                n %= 100
            if n > 19:
                re.append(tens[n / 10 -2])
                n %= 10
            if n:
                re.append(to19[n]) 
            return re
        re = []
        if num / 10 ** 9:
            re += (trans(num/10 ** 9) + ['Billion'])
            num %= 10 ** 9
        if num / 10 ** 6 :
            re += (trans(num/10 ** 6) + ['Million'])
            num %= 10 ** 6
        if num / 10 ** 3:
            re += (trans(num/10 ** 3) + ['Thousand'])
            num %= 10 ** 3
        if num:
            re += (trans(num))
        return ' '.join(re) if re else 'Zero'
