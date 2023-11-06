import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Integer[] newArray = Arrays.stream(numbers).boxed().toArray(Integer[]::new);
     
        Arrays.sort(newArray, Collections.reverseOrder());
        
        answer = newArray[0] * newArray[1];

        
        return answer;
    }
}