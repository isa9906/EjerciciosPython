def sumaDigitos (n):
 
    if(abs(n)==10):
        return 1
    if(abs(n)<10):
        return n
    
    return abs(n)%10 + int(sumaDigitos(abs(n)/10))
n= int(input())
print (sumaDigitos(n))
        
