nums = [0,4,0,0,2,7,0,9,0,18]

'''
create new array and append no zero element .afterward place in original and remaining with zero
'''
def approach1(nums):
    n = []
    for i in range(len(nums)):
        if nums[i]!=0:
            n.append(nums[i])


    for j in range(len(n)):
        nums[j]=n[j]
        
    for j in range(len(n),len(nums)):
        nums[j]=0
        
        
        
'''
 two pointer i and j where i is the first zero and j is the first non zero and than swap then again find i and j

'''       
        
def approach2(nums):
        i=0
        while i<len(nums) and nums[i]!=0:
            i+=1
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                while i<len(nums) and nums[i]!=0:
                   i+=1
            j+=1
'''
count the number zero before non zero element and swap with first zero
'''         
def approach3(nums):
        co=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                co+=1
            else:
                te= nums[i]
                nums[i]=0
                nums[i-co]=te
            i+=1
            
print(nums)