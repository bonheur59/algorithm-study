class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        
        if(n > slice){
            if (n % slice == 0) {
                answer = n / slice;
            } else {
                answer = (n / slice) + 1;   
             }
        } else 
            answer = 1;
        
        return answer;
    }
}