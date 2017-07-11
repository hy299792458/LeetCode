class Solution(object):
    def validIPAddress(self, IP):
        def check4(num):
            if num.isdigit() and 0 <= int(num) <= 255 and str(int(num)) == num:
                return True
            else:
                return False
        def check6(num):
            if len(num) > 4 or len(num) == 0:
                return False
            if not all(char.isdigit() or char.lower() in 'abcdef' for char in num):
                return False
            return True
        
        ipv4 = IP.split('.')
        if len(ipv4) == 4 and all(check4(seg) for seg in ipv4):
            return 'IPv4'
        ipv6 = IP.split(':')
        if len(ipv6) == 8 and all(check6(seg) for seg in ipv6):
            return 'IPv6'
        return 'Neither'
