import math
def isprime(n):
    if(n==0 or n==1):
        return False
    elif(n%2==0 or n%3==0):
        return False
    else:
        for i in range(5,int(math.sqrt(n)),6):
            if n%i==0 or n%(i+2)==0:
                return False
    return True
print(isprime(59))