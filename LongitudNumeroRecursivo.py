def longitudNumero(n):
    if (abs(n)<10):
        return 1
    else:
        return 1+ int(longitudNumero(abs(n)/10))

n=int(input())
print (longitudNumero(n))
