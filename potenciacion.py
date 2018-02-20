def potenciacion(n,m):
    if(m==1):
        return n
    else:
        return n*potenciacion(n,m-1)

n = int(input())
m = int(input())
print(potenciacion(n,m))
    
