class MinSubArrayLen {
    public int minSubArrayLen(int target, int[] nums) {
        
        int ans = Integer.MAX_VALUE;
        // for(int i=0;i<nums.length;i++){
        //     int cl = 0,sum=0;
        //     for(int j=i;j<nums.length;j++){
        //         sum+=nums[j];
        //         cl++;
        //         if(sum>=target){
        //             ans = Math.min(ans,cl);
        //             cl=0;
        //             sum=0;
        //         }
        //     }
        // }

        int cl=0,sum=0;
        int i=0,j=0;
        while(j<nums.length){
            sum+=nums[j];
            cl++;
            if(sum>=target){
                ans = Math.min(ans,j-i+1);
                while(i<=j && sum>=target){
                    ans = Math.min(ans,j-i+1);
                    sum-=nums[i];
                    i++;
                    cl--;
                }
               
            }
            j++;
        }
        return ans==Integer.MAX_VALUE ? 0 : ans;
    }
}