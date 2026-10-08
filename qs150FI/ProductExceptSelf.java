class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        int p = 1;
        ans[0] = p;
        for(int i=1;i<n;i++){
            p *= nums[i-1];
            ans[i] = p;
        }
        p=1;
        for(int i=n-2;i>=0;i--){
            p *= nums[i+1];
            ans[i] = ans[i]*p;
        }
        return ans;
    }
}