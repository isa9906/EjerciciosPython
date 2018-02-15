def longitudNumero(n):
    if ((abs(n))<10):
        return 1
    else:
    
        return 1+ int(longitudNumero(abs(n)/10))
def invertirNumero(n):
    if (n<10):
        return n
    else:
        return n%10*(10**(longitudNumero(n)-1))+ invertirNumero(int(n/10))
n= int(input())
print(invertirNumero(n))
