class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        int temp = x - 0;
        
        while(temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        return  (x % sum == 0) ? true : false;
        
        
    }
}

