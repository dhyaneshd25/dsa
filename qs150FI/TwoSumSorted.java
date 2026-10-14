class TwoSumSorted {
    public int[] twoSum(int[] numbers, int target) {
            int i=0,j=numbers.length-1;
            // for(int p=0;p<numbers.length;p++){
            //     for(int q=p+1;q<numbers.length;q++){
            //         if(numbers[p]+numbers[q]==target){
            //             return new int[]{p+1,q+1};
            //         }
            //     }
            // }
            while(i<j){
                int val = numbers[i]+numbers[j];
                if(val==target){
                    return new int[]{i+1,j+1};
                }else if(val>target){
                    j--;
                }else{
                    i++;
                }
               
            }

            return null;
    }
}