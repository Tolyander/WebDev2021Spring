import math

n = int(input())
cnt = 0

while cnt < int(math.sqrt(n)):
    cnt += 1
    print(cnt * cnt)