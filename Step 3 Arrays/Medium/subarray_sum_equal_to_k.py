nums = [1,2,3]
k = 3

#brute force O(n^2) and space O(1)
def subarraySum(nums, k):
        ans =0 
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==k:
                    ans+=1

        return ans
print(subarraySum(nums,k))


#brute force O(N) and space O(N)
def subarraySum_approach2(nums, k):
        ans =0 
        su=0
        mp=dict()
        mp[0]=1
        for i in range(len(nums)):
            su+=nums[i]
            if su-k in mp.keys():
                ans+=mp[su-k]
            if su not in mp.keys():
                mp[su]=1
            else:
                mp[su]+=1 

        return ans
print(subarraySum_approach2(nums,k))