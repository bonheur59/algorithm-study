import sys

n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

negative, positive = [], []
for i in range(len(books)):
    if books[i] > 0:
        positive.append(books[i])

    if books[i] < 0:
        negative.append(books[i])
        
negative.sort()
positive.sort(reverse=True)

max_value = 0
for book in books:
    if abs(max_value) < abs(book):
        max_value = book

result = 0
for i in range(0, len(negative), m):
    if negative[i] != max_value:
        result += abs(negative[i])
for i in range(0, len(positive), m):
    if positive[i] != max_value:
        result += positive[i]

answer = result * 2 + abs(max_value)

print(answer)