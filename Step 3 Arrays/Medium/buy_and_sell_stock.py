prices=[7,1,5,3,6,4]



#brute force O(n^2)
ans = 0
for i in range(len(prices)):
            b=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]>b:
                    b=prices[j]
            ans=max(ans,b-prices[i])
print(ans)



#optimal O(n)
b,s=prices[0],prices[0]
ans = 0 
for i in range(1,len(prices)):
            if s>prices[i]:
                s=prices[i]
            s=max(s,prices[i])
            b=min(b,prices[i])
            ans = max(ans,s-b)
print(ans)