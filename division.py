def division(n,m):
    if(m<=n):
        return 1 + division(n-m,m)
    else:
        return 0

n = int(input())
m = int(input())
print(division(n,m))

