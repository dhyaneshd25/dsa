class JumpGame {
    
    public boolean canJump(int[] nums) {
        int n=nums.length;
        int[] dp =new int[n];
    //     return jump(nums,0,n,dp);
        
    // }
    // public boolean jump(int[] arr,int ind,int l,int[] dp){
    //     if(ind==l-1){
    //         return true;
    //     }
    //     if(arr[ind]==0){
    //         return false;
    //     }
    //     if(dp[ind]!=0){
    //         return true;
    //     }
    //     for(int i=ind+1;i<=arr[ind]+ind;i++){
    //         if(i<l && jump(arr,i,l,dp)){
    //             dp[i] = 1;
    //             return true;
    //         }
    //     }
    //     dp[ind] = 0;
    //     return false;
    // }
    int ans = 0;
    for(int i=0;i<n;i++){
        if(ans<0){
            return false;
        }else if(nums[i]>ans){
            ans = nums[i];
        }
        ans--;
     
    }

        return true;
    }
}/*98 */