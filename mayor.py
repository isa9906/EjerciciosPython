def MayorDigito (n):
    if((abs(n==0))):
        return 0
    else:
        
        if(abs(n)%10< int(MayorDigito(int(abs(n)/10)))):
            return int(MayorDigito(int(abs(n)/10)))
        else:
            return abs(n)%10;
    

n= int(input())
print (MayorDigito(n))
        
