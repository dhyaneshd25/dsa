class RemoveDuplicate2 {
    public int removeDuplicates(int[] nums) {
        int k=0;
        int i=0;
        int n=nums.length;
        while(i<n){
            int temp = nums[i];
            int co = 0;
            while(i<n && nums[i]==temp){
                if(co<2){
                    nums[k] = temp;
                    k++;
                }
                co++;
                i++;
            }
        }
        return k;
    }
}