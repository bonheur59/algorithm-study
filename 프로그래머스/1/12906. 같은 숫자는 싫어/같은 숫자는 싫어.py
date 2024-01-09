def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for i in range(len(arr)):
        if arr[i] not in answer:   #i이 answer에 없는 경우
            answer.append(arr[i])
        else:
            if arr[i-1] != arr[i]:
                answer.append(arr[i])
            
        
    return answer