class JumpGame2 {
    public int jump(int[] nums) {
        int n = nums.length;
    //     int[] dp = new int[n];
    //     Arrays.fill(dp,-1);
    //     return jp(0,0,nums,dp);
    // }
    // public int jp(int c,int ind,int[] nums,int[] dp){
    //     if(ind>=nums.length-1){
            
    //         return 0;
    //     }
    //     if(dp[ind]!=-1){
    //         return dp[ind];
    //     }
    //     int s=ind+1,e=ind+nums[ind];
    //     int ans=100000;
    //     for(int i=s;i<=e && i<nums.length;i++){
    //         int st = jp(c+1,i,nums,dp);
    //         ans=Math.min(ans,1+st);
    //     }
    //     dp[ind] = ans;
    //     return ans;
    // }
    if(n<=1) return 0;
    int ans = 0;
    int f = 0;
    int ci = 0;
    for(int i=0;i<n;i++){
        f = Math.max(f,i+nums[i]);
        if(i==ci){
            ans++;
            ci = f;
            if(ci>=n-1){
                break;
            }
        }
    }
    return ans;
    }
}