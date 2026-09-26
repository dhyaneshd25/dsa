class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // int i=m-1;
        // int j=n-1;
        // int k=m+n-1;
        // for(int p = m,q=0;p<m+n;p++,q++){
        //     nums1[p]=nums2[q];
        // }
        // Arrays.sort(nums1);

       int i=m-1;
       int j=n-1;
       int k=m+n-1;
       while(k>=0 && i>=0 && j>=0){
        if(nums1[i]>=nums2[j]){
            nums1[k] = nums1[i];
            i--;
        }else{
            nums1[k] = nums2[j];
            j--;
        }
        k--;
       }
        while(k>=0 && j>=0){
            nums1[k]=nums2[j];
            k--;
            j--;
        }
    }
}