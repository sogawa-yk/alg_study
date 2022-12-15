N = int(input())
A = list(map(int, input().split()))
f = True
cnt = 0

while f:
    for a in A:
        if not a%2 == 0:
            f = False
            break
    if f:
        A = list(map(lambda x: x//2, A))
        cnt += 1

print(cnt)