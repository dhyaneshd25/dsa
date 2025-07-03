nums = [2,2,1,1,1,2,2]



# moore voting algo o(n) and space O(1)
ans = nums[0]
co=1
i=1
while i<len(nums):
            if co==0:
                ans=nums[i]
                co=1
            elif nums[i]==ans:
                co+=1
            else:
                co-=1
            i+=1
nums = [2,2,1,1,1,2,2]        
# sorting
nums.sort()
ans = nums[len(nums)//2]

#here we can also use hashmap of counting