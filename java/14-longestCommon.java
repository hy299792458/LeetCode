public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){
            return "";
        }else if(strs.length == 1){
            return strs[0];
        }
        int end = 0;
        while(end < strs[0].length()){
            for(int i = 1; i < strs.length; i++){
                if(end >= strs[i].length() || strs[i].charAt(end) != strs[0].charAt(end)){
                    return strs[0].substring(0, end);
                }
            }
            end ++;
        }
        return strs[0];
    }
}
