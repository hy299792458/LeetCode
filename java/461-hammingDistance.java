public class Solution {
    public int hammingDistance(int x, int y) {
        int res = 0;
        int d = x ^ y;
        while(d != 0){
            res += d % 2;
            d /= 2;
        }
        return res;
    }
}
