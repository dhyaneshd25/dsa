class TrapRainWater {
    public int trap(int[] height) {
        int n=height.length;
        int i=0;
        int ans=0;
        while(i<n && height[i]==0) i++;
        int j=n-1;
        while(j>=0 && height[j]==0) j--;
        if(i>=n || j<0) return 0;
        int mh = height[i],in=i;
        for(int k=i+1;k<=j;k++){
            if(height[k]>mh){
                mh= height[k];
                in=k;
            }
        }

        int h=0;
        for(int k=i;k<in;k++){
            if(height[k]>h){
                h=height[k];
            }else{
                ans+=h-height[k];
            }
        }
        h=0;
        for(int k=j;k>in;k--){
            if(height[k]>h){
                h=height[k];
            }else{
                ans+=h-height[k];
            }
        }
        // int j=i;
        // int ps = -1;
        // while(j<n){
        //     if(height[i]>=height[j]){
        //         if(i<j && height[j]>height[j-1]){
        //             int temp=0;
        //             for(int k=i+1;k<j;k++){
        //                 if(height[k]-height[j]>0){

        //                 ans+=height[k]-height[j];
        //                 temp+=height[k]-height[j];
        //                 }
        //             }
        //             if(temp!=0){
        //             ps=temp;
        //             }
        //         }
        //         j++;
        //     }else{
        //         for(int k=i+1;k<j;k++){
        //             ans+=height[i]-height[k];

        //         }
        //         if(ps!=-1){
        //             ans-=ps;
        //             ps=-1;
        //         }
        //         i=j;
        //     }
        // }

    return ans;
        
    }
}