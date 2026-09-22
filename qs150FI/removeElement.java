class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int n=nums.length;
        // int i=0,j=n-1;
        // int co = 0;
        // for(int k=0;k<n;k++){
        //     if(nums[k]==val){
        //         co++;
        //     }
        // }
        // while(i<j){
        // while(i<j && j>=0 && nums[j]==val) j--;
        // while(i<j &&i<n && nums[i]!=val) i++;
        //     int temp = nums[i];
        //     nums[i]=nums[j];
        //     nums[j]=temp;
           
        // }
        // return n-co;

        int k=0;
        for(int i=0;i<n;i++){
            if(nums[i]!=val){
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}