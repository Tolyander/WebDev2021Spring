n = int(input())
cnt = 1
if(n == cnt):
    print ("YES")
    exit()

while cnt * 2 <= n:
    cnt *= 2
    if(n == cnt):
        print ("YES")
        exit()

print ("NO")