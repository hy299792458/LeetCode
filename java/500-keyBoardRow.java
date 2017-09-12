public class Solution {
    public String[] findWords(String[] words) {
        String[] rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        Map<Character, Integer> map = new HashMap();
        for(int i = 0; i < 3; i ++){
            for (char c: rows[i].toCharArray()){
                map.put(c, i);
            }
        }
        List<String> res = new LinkedList<>();
        for (String word : words){
            if(word.equals("")) continue;
            int index = map.get(word.toLowerCase().charAt(0));
            for (char c: word.toLowerCase().toCharArray()){
                if(map.get(c) != index){
                    index = -1;
                    break;
                }
            }
            if (index!=-1) res.add(word);
        }
        return res.toArray(new String[0]);
    }
}
