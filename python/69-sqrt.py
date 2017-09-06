class Solution(object):
    def mySqrt(self, x):
        i=1.0;
    	while(True):
    		j=(i+x/i)/2.0;
    		if(abs(i-j)< 0.000000000005):
    			break;
    		i=j;
    	return int(j);