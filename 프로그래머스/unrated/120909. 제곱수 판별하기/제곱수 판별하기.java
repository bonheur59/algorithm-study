class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = 0;
        
        for(int i=1; i <= n; i++){
            if (n % i ==0){
                cnt++;
            }
        }
        
        
        return answer = (cnt % 2 != 0) ? 1 : 2;
    }
}