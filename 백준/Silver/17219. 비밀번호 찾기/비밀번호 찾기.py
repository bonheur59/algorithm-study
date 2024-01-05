import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dict = {}

#입력 받은 n번의 숫자만큼 사이트의 주소와 비밀번호를 딕셔너리에 넣음
for _ in range(n):
    id, pw = map(str, sys.stdin.readline().rstrip().split())
    dict[id] = pw

#찾을 이메일을 입력받고 dict의 key값으로 넣어서 value를 출력
for _ in range(m):
    searchAddr = str(sys.stdin.readline().rstrip())
    print(dict[searchAddr])
