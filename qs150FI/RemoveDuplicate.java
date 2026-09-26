class RemoveDuplicate{
    public int removeDuplicates(int[] nums) {
       int k=0;
       int n=nums.length;
    //    int i=0,j=1;
    //    while(i<j && j<n){
    //     if(nums[i]!=nums[j]){
    //         k++;
    //         i++;
    //         j++;
    //     }else{
    //         for(int p=j;p<n-1;p++){
    //             int temp = nums[p];
    //             nums[p] = nums[p+1];
    //             nums[p+1] = temp;
    //         }
    //         n--;
    //     }
    //    }
    //    return k+1;

    int i=0;
    while(i<n){
        nums[k]=nums[i];
        k++;
        int  temp = nums[i];
        while(i<n && nums[i]==temp) i++;
    }

    return k;
    }
}