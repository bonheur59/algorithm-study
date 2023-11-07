class Solution {
    public int solution(int[] dot) {
    
    int answer = 0;
        
    int x = dot[0] > 0 ? 1 : 0;
    int y = dot[1] > 0 ? 1 : 0;
        
    if(x+y == 2){
        return 1;
    } else if(x+y == 0){
        return 3;
    } else{
        if (x<y){
            return 2; 
        } else{
            return 4;
        }
    }
    }
}