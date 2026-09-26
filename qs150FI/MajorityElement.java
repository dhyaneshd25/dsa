class MajorityElement {
    public int majorityElement(int[] nums) {
        int ans = nums[0];
        int co=1;
        for(int i=1;i<nums.length;i++){
           if(nums[i]==ans){
            co++;
           }else{
            co--;
           }
           if(co==0){
            ans = nums[i];
            co=1;
           }

        }
        return ans;
    }
}