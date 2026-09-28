class BestTimeBuySellStock {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        int ans=0;
        // for(int i=0;i<n;i++){
        //     for(int j=i+1;j<n;j++){
        //         ans = Math.max(ans,prices[j]-prices[i]);
        //     }
        // }
        int min = prices[0];
        for(int i=1;i<n;i++){
            min=Math.min(min,prices[i]);
            ans = Math.max(ans,prices[i]-min);
        }
        return ans;
    }
}