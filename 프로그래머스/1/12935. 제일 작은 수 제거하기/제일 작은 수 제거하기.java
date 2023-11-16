import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
     
        if(arr.length > 1) {
            int[] answer = new int[arr.length-1];
            int min = arr[0];
            int cnt = 0;
            
            for(int i=0; i < arr.length; i++) {
                min = Math.min(min, arr[i]);
            }
            
            for (int i= 0; i < arr.length; i++) {
                if(arr[i] == min) {
                  continue;
                }
               answer[cnt++] = arr[i];
            }
            
            return answer;
            
        } else {
            int[] answer = {-1};
            return answer;
        }
    }
}