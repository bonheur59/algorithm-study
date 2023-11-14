import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int cnt = 0;
        
        ArrayList<Integer> numArr = new ArrayList<>();
       
        for(int i : arr) {
            if(i % divisor == 0) {
                numArr.add(i);
            } 
        }
        
        if(numArr.size() == 0) {
             numArr.add(-1);
        }
        
        int[] answer = new int[numArr.size()];
        
        for (int i = 0 ; i < numArr.size() ; i++) 
        answer[i] = numArr.get(i).intValue();
        
        Arrays.sort(answer);
     
        return answer;
    }
}