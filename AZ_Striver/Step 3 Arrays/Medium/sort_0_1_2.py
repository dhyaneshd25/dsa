nums = [2,0,2,1,1,0]

#brute force :- sort the array O(nLogn)

#optimal O(n) and space O(1)
co = [0,0,0]
for i in range(len(nums)):
            co[nums[i]]+=1
for i in range(co[0]):
            nums[i]=0
j=co[0]
for i in range(co[1]):
            nums[j]=1
            j+=1
for i in range(co[2]):
            nums[j]=2
            j+=1
            
            
#optimal O(n) and space O(1)
# Dutch National Flag Algo
'''
note :- not increament the iteration pointer when we get 2 because there is a possible where 1 can be neglected
'''
i,j=0,len(nums)-1
while i<len(nums) and nums[i]==0:
            i+=1
while j>=0 and nums[j]==2:
            j-=1
k=i
while k<=j:
            if nums[k]==0:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1
                k+=1
            elif nums[k]==2:
                nums[k],nums[j]=nums[j],nums[k]
                j-=1 #
            else:
                k+=1