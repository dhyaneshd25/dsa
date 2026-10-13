class ZigzagConversion {
    public String convert(String s, int numRows) {
        if(numRows==1) return s;
        StringBuilder ans = new StringBuilder();
        // StringBuilder temp[] = new StringBuilder[numRows];
        // for(int i=0;i<numRows;i++) temp[i] = new StringBuilder();
        // int n=s.length(),cr=0,d=0;
        // for(int i=0;i<n;i++){
        //     char ch = s.charAt(i);
        //     if(cr==numRows){
        //         cr = numRows-2;
        //         d=1;
        //     }
        //     if(cr==0){
        //         d=0;
        //     }
        //     temp[cr].append(ch);
        //     if(d==0){
        //         cr++;
        //     }else{
        //         cr--;
        //     }
        // }
        // for(StringBuilder i:temp){
        //     ans.append(i);
        // }
        for(int i=0;i<numRows;i++){
            for(int j=i;j<s.length();j+=(2*(numRows-1))){
                ans.append(s.charAt(j));
                 if (i > 0 && i < numRows - 1 && j + (2 * (numRows - 1)) - (2 * i) < s.length()) {
                    ans.append(s.charAt(j + (2 * (numRows - 1)) - (2 * i)));
                }
            }
        }


        return ans.toString();
    }
}