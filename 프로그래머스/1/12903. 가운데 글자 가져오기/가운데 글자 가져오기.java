class Solution {
    public String solution(String s) {
        String answer = "";
        int sLength = s.length()/2;
 
        answer = (s.length() % 2 == 0) ? 
            s.substring(sLength-1, sLength+1) : s.substring(sLength, sLength+1);
        
        return answer;
    }
}