import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String[] numArray = Long.toString(n).split("");
        
        Arrays.sort(numArray);
        
        StringBuilder sb = new StringBuilder();
        
        for (String s : numArray) sb.append(s);
        
        answer = Long.parseLong(sb.reverse().toString());
        
        return answer;
        
        
        
    }
}