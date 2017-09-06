class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1==p2==p3==p4:return False
        def leng(p):
            return p[0]**2+p[1]**2
            
        p12=[p2[0]-p1[0],p2[1]-p1[1]];
        p23=[p3[0]-p2[0],p3[1]-p2[1]];
        p34=[p4[0]-p3[0],p4[1]-p3[1]];
        p41=[p4[0]-p1[0],p4[1]-p1[1]];
        p24=[p4[0]-p2[0],p4[1]-p2[1]];
        p13=[p3[0]-p1[0],p3[1]-p1[1]];
        p=[p12,p23,p34,p41,p24,p13];
        length=[];
        for i in range(6):
            length.append(leng(p[i]));
        length=sorted(length);
        if length[5]==length[4]==2*length[3]==2*length[2]==2*length[1]==2*length[0]:
            return True 
        else: return False
        
            
            
