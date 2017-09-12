public class Solution {
    public boolean isPowerOfTwo(int n) {
        return (((n - 1) & n) == 0 && n > 0);
    }
}
