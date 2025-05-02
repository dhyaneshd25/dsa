'''

4444444
4333334
4322234
4321234
4322234
4333334
4444444

'''
n = int(input())


# for i in range(0,2*n-1):
#     if(i<n):
#         k=n
#         co=i
#         for j in range(0,i):
#             print(k,end='')
#             k-=1
    
#         while(co<n):
#             print(k,end="")
#             co+=1
#         while(co<2*n-i-1):
#             print(k,end="")
#             co+=1
#         k+=1
#         while(k<=n):
#             print(k,end='')
#             k+=1
#     else:
#         k=n
#         co=2*n-i
#         for j in range(i,2*n-1):
#             print(k,end='')
#             k-=1
#         k+=1
#         while(co<=n):
#             print(k,end="")
#             co+=1
#         for j in range(2*n-i+1,i):
#             print(k,end='')
#         # for j in range(i,2*n-1):
#         #     print(k,end='')
#         #     k+=1   
     
#     print()
val,v,va,vv=2*n-1,n,3 ,2   
for i in range(0,2*n-1):
   
    if i<n:
        k=n
        for m in range(0,i):
            print(k,end='')
            k-=1
        for j in range(0,val):
            print(v,end='')
        val-=2
        v-=1
        k+=1
        while(k<=n):
            print(k,end="")
            k+=1
    else:
        k=n
        for j in range(i,2*n-1):
            print(k,end="")
            k-=1
        for j in range(0,va-1):
            print(vv,end='')
        vv+=1
        va+=2
        k+=2
        while k<=n:
          print(k,end='')
          k+=1
    print()
      
   
co=1
l=n
ne=1
for i in range(0,2*n-1):
    if i==0 or i==2*n-2:
        for j in range(0,2*n-1):
            print(n,end='')
    elif i<n:
        val=n
        for j in range(0,co):
            print(val,end='')
            val-=1
        for j in range(0,l-1):
            print(val,end='')
        l-=1
        co+=1
        for j in range(0,l-1):
            print(val,end='')
        val+=1
        while(val<=n):
            print(val,end='')
            val+=1
    else:
        val=n
        co-=1
        for j in range(0,co):
            print(val,end='')
            val-=1
        val+=1
        
        for j in range(0,l):
            print(val,end='')
        l+=1
        for j in range(0,ne):
            print(val,end='')
        ne+=1
        val+=1
        while(val<=n):
            print(val,end='')
            val+=1
    
    print()       
        