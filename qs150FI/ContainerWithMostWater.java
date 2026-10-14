class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int i=0,j=height.length-1;
        int ans=0;
        while(i<j){
            int mh = Math.min(height[i],height[j]);
            ans = Math.max(ans,(j-i)*mh);
            if(height[i]>=height[j]){
                j--;
            }else{
                i++;
            }
        }
        return ans;
    }
}