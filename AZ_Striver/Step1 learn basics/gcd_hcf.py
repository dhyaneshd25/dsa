def gcd_hcf(a,b):
    if b==0:
        return a
    else:
        return gcd_hcf(b,a%b)
    
print(gcd_hcf(89,4))

def gcd_hcf2(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        elif(a<b):
            b=b-a
    return a
print(gcd_hcf2(89,4))