import java.util.*;

class Solution {
    public int[] solution(long n) {
        String numStr = n + "" ;
        
        int[] answer = new int[numStr.length()];
            
        for(int i = numStr.length()-1; i >= 0; i--){
       answer[numStr.length()-1-i] = numStr.charAt(i) - '0';
          
        }
        return answer;
    }
}