import sys
n=int(sys.stdin.readline())

before=[] #터널 들어가기 전 순위
for i in range(n):
    before.append(sys.stdin.readline().rstrip())

after=[] #터널 나온 후 순위
for i in range(n):
    after.append(sys.stdin.readline().rstrip())

cnt=0
for i in range(n):
    if before[i]!=after[i]: #들어가기 전과 나온 후의 i순위가 다르면,
        cnt+=1 #추월을 했다는 것이다.
        toPop=before.index(after[i]) #추월한 놈의 before에서의 순위
        before.insert(i,before.pop(toPop)) #i순위로 이놈을 이동.

print(cnt)