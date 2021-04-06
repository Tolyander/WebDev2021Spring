a = int(input())
b = int(input())

# a_rev = a[::-1]
# ans = False

# if a == a_rev and len(a) == 4:
#     ans = True

# if ans and b == 1:
#     print("YES")
# elif ans == False and b == -1: 
#     print("YES")
# else: 
#     print("NO")

if a != 1 and b != 1:
    print("YES")
elif a == 1 and b == 1:
    print("YES")
else: print("NO")