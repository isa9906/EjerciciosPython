def producto (n,m):
    if (n==0 or m==0):
        return 0
    if n==1:
        return n
    return n+ int(producto(n,m-1))
n= int(input())
m= int(input())
print(producto(n,m))
