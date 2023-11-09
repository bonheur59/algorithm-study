import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCnt= 0;
        int yCnt = 0;
                
        for(char x : s.toCharArray()){
            if (Character.toLowerCase(x) == 'p'){
                pCnt++;
            } 
            if (Character.toLowerCase(x) == 'y'){
                yCnt++;
            }
        }
        answer = (pCnt == yCnt) ? true : false ;

        return answer;
    }
}