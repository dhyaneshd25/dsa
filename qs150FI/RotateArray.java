class RotateArray {
    public void reverse(int nums[],int i,int j){
        while(i<=j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k%=n;
        // int arr[] = new int[n-k];
        // for(int q=0;q<n-k;q++){
        //     arr[q]=nums[q];
        // }
        // int i=0;
        // int j=n-k;
        // int p=0;
        // while(j<n){
        //     nums[i++]=nums[j++];
        // }
        // while(i<n){
        //     nums[i++]=arr[p++];
        // }
       
        reverse(nums,0,n-1);
        reverse(nums,0,k-1);
        reverse(nums,k,n-1);
       
    }
}