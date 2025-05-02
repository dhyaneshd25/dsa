'''
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    int arr[] = {1,3,2};
    
    next_permutation(arr,arr+3);//using in-built function of C++
    
    cout<<arr[0]<<" "<<arr[1]<<" "<<arr[2];
    
    return 0;
}

'''
nums = [1,1,5]
def allp(nums,temp,ans):
        if len(temp)==len(nums):
            ans.append(temp[:])
            return
        for num in nums:
            if num in temp:
                    continue
            temp.append(num)
            allp(nums,temp,ans)
            temp.pop()
      
def permute(nums):
        ans = []
        allp(nums,[],ans)
        return ans

nums = [4,5,2]

ans=permute(nums)
print(ans)

#brute force  O(n*n!)  because we check all element for each premutation(n!)




#optimal O(n)
'''
find the break point (1<2) then swap that index with the index which is greater than it but smaller amongs after it
sort the remaining list
'''
def approach2(nums):
        i=len(nums)-2
        ii=-1
        while i>=0:
            if nums[i]<nums[i+1]:
                ii=i
                break
            i-=1
        if ii==-1:
            nums.sort()
            return nums
        ind=-1
        k=len(nums)-1
        while k>ii:
            if nums[k]>nums[ii]:
                ind=k
                break
            k-=1

        if ind!=-1 and ind<len(nums):
            nums[ii],nums[ind]=nums[ind],nums[ii]

        nums[ii+1:len(nums)]=sorted(nums[ii+1:len(nums)])
        return nums
ans = approach2(nums)



