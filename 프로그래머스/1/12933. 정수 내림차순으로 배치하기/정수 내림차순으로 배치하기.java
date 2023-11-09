import java.util.*;

class Solution {
    public long solution(long n) {
        String[] numArray = String.valueOf(n).split("");      
        Arrays.sort(numArray);
        
        StringBuilder sb = new StringBuilder();
        for (String s : numArray) sb.append(s);
        
        return  Long.parseLong(sb.reverse().toString());
    }
}