public class Solution {
    public int findComplement(int num) {
        int res = 1;
        while (res < num){
            res <<= 1;
            res += 1;
        }
        return res - num;
    }
}
