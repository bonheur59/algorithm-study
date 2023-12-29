def solution(s):
    answer = 0
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i, number in enumerate(numbers):
        s = s.replace(number, str(i))
        
    return int(s)