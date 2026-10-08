class GasStationCompleteCircuit {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        // for(int i=0;i<n;i++){
        //     boolean ck = true;
        //     int ct = 0;
        //     for(int j=i;j<n;j++){
        //         ct+=gas[j];
        //         if(cost[j]>ct){
        //             ck=false;
        //             break;
        //         }
        //         ct -= cost[j];
        //     }
        //     for(int j=0;j<i;j++){
        //         ct+=gas[j];
        //         if(cost[j]>ct){
        //             ck=false;
        //             break;
        //         }
        //         ct -= cost[j];
        //     }
        //     if(ck){
        //         return i;
        //     }
        // }
        // return -1;
        int s = 0, td = 0, d =0;
        for(int i=0;i<n;i++){
            td+=gas[i]-cost[i];
            d+=gas[i]-cost[i];
            if(d<0){
                d=0;
                s=i+1;
            }
        }
        return td>=0 ? s : -1;    
    }
}