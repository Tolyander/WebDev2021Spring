n = int(input())
cnt = 1

while cnt < n:
    cnt += 1
    if(n % cnt == 0):
        print(cnt)
        exit()