import java.util.Arrays;

class Candy {
    // class IP{
    //     int val;
    //     int index;
    //     IP(int val,int index){
    //         this.val = val;
    //         this.index = index;
    //     }
    // }
    // public void print(int arr[]){
    //     for(int i:arr){
    //         System.out.print(i+" ");
    //     }
    //         System.out.println();
    // }
    public int candy(int[] ratings) {
        int ans[] = new int[ratings.length];
        Arrays.fill(ans,1);
        // List<IP> arr = new ArrayList<>();
        // for(int i=0;i<ratings.length;i++){
        //     IP t = new IP(ratings[i],i);
        //     arr.add(t);
        // }
        // Collections.sort(arr,(a,b)->{
        //     if(a.val!=b.val){
        //         return Integer.compare(a.val,b.val);
        //     }
        //     return Integer.compare(a.index,b.index);
        // }
        // );
        // for(int i=1;i<arr.size();i++){
        //     IP el = arr.get(i);
        //     int in = -1;
        //     boolean ck = false;
        //     for(int j=0;j<i;j++){
        //         IP ne = arr.get(j);
        //         if(el.val>ne.val && (el.index+1==ne.index || el.index==ne.index+1)){
        //             ck =true;
        //             in =Math.max(ans[ne.index],in);

        //         }
        //     }
        //     if(ck){
        //         ans[el.index] =in+1;
        //     }
        // }
        // int res = 0;
        // for(int i:ans){
        //     res+=i;
        // }
        // print(ans);
        // return res;

        for(int i=1;i<ratings.length;i++){
            if(ratings[i]>ratings[i-1]){
                ans[i]=ans[i-1]+1;
            }
        }
        for(int i= ratings.length-2;i>=0;i--){
            if(ratings[i+1]<ratings[i]){
                ans[i] =Math.max(ans[i],ans[i+1]+1);
            }
        }
        int res = 0;
        for(int i:ans){
            res+=i;
        }
        return res;
      
    }
}