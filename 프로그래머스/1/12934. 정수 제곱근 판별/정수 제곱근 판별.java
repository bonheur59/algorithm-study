class Solution {
    public long solution(long n) {
        long answer = 0;
        long sr = (int)Math.sqrt(n);


        if(n / sr == sr && n % sr == 0)  {
            return (long)(sr + 1) * (sr + 1);
        } else{
            return -1;
        }
    }
}
