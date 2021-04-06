n = int(input())
k = 1
cnt = 0

while n > k:
    k *= 2
    cnt += 1

print(cnt)