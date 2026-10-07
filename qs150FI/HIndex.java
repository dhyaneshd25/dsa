class HIndex {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int ans=Integer.MIN_VALUE;
        // for(int i=citations.length;i>0;i--){
        //     int co=0;
        //     for(int j=0;j<citations.length;j++){
        //         if(citations[j]>=i){
        //             co++;
        //         }
        //     }
        //     if(co>=i){
        //         // ans = Math.max(ans,i);
        //         ans = i;
        //         break;
        //     }
        // }
        // Arrays.sort(citations);
        
        // for(int i=citations.length-1,j=1;i>=0;i--,j++){
        //     if(citations[i]>=j){
        //         ans = Math.max(ans,j);
        //     }
        // }
        // return ans == Integer.MIN_VALUE ? 0 : ans;
        int count[] = new int[n+1];
        for(int j:citations){
            count[Math.min(j,n)]++;
        }
        int p =0;
        for(int i=n;i>=0;i--){
            p+=count[i];
            if(p>=i){
                return i;
            }
        }
        return 0;
    }
}