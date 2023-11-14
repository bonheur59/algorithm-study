class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int starLength = phone_number.length() - 4;
        
        for(int i = 0; i < phone_number.length(); i++){
            if(i < starLength){
                answer += "*";
            } else {
                answer += String.valueOf(phone_number.charAt(i));
            }
        }
        
        return answer;
    }
}