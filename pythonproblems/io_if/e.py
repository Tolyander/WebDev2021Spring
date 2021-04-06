a = int(input())
b = int(input())

s = a * b % 109

if s == 0:
    print(s)
    exit()

if a < 0:
    print(109 - (109 - abs(s)))
else:
    print(s)