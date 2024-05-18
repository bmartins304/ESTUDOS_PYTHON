

def fatorial(a=1, show=False):
    f2=1
    f1 = a
    f2 = 1
    if show == True:
        while f1 > 0:
            f3 = f1
            f2 = f2 * f1
            f1 -= 1
            print(f3, end=' x ')
        return f2
    elif show == False:
        while f1 > 0 :
            f2 *= f1
            f1-=1
        return f2
    
print(fatorial(5))
