nums = [9,1,4,7,3,-1,0,5,8,-1,6]

#brute force O(n^2)

#better approach O(NLogN) because of sorting
def approchsorting(nums):
        if len(nums)==0:
            return 0
        nums.sort()
        ans=1
        co=1
        i=1
        while i<len(nums):
            if nums[i-1]+1==nums[i]:
                co+=1
                ans=max(co,ans)
            elif nums[i-1]!=nums[i]:
                co=1
            i+=1

        return ans


#optimal O(N) and space O(N)
def longestConsecutive(nums):
        if len(nums)==0:
            return 0
        st =set(nums)
        ans = 0
        for i in st:
            if i-1 not in st:
                co=0
                x=i
                while x in st:
                   co+=1
                   x+=1
                ans=max(ans,co)
        return ans

