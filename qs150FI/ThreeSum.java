import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);
        // for(int i=0;i<n;i++){
        //     for(int j=i+1;j<n;j++){
        //         for(int k=j+1;k<n;k++){
        //             if(nums[i]+nums[j]+nums[k]==0){
        //                 List<Integer> temp = new ArrayList<>();
        //                 temp.add(nums[i]);
        //                 temp.add(nums[j]);
        //                 temp.add(nums[k]);
        //                 if(!ans.contains(temp)){
        //                   ans.add(temp);
        //                 }
        //             }
        //         }
        //     }
        // }
        // return ans;
        Set<List<Integer>> res = new HashSet<>();
        for(int i=0;i<n;i++){
            int j=i+1,k=n-1;
            while(j<k){
          
                if(nums[i]+nums[j]+nums[k]==0){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(nums[k]);
                    // if(!ans.contains(temp)){
                    //     ans.add(temp);
                    // }
                    // ans.add(temp);
                    res.add(temp);
                    j++;
                    k--;
                }else if(nums[i]+nums[j]+nums[k]>0){
                    k--;
                }else{
                    j++;
                }
            }
        }
        return new ArrayList<>(res);
    }
}