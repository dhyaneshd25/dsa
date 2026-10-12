class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        // Arrays.sort(strs,(a,b)->Integer.compare(a.length(),b.length()));
        String ans=strs[0];
        for(int i=1;i<strs.length;i++){
            // ans = answer(ans,strs[i]);   
            while(!strs[i].startsWith(ans)){
                ans = ans.substring(0,ans.length()-1);
                if(ans.equals("")){
                    return "";
                }
            }         
        }
        return ans;
    }
    String answer(String a,String b){
        StringBuilder ans=new StringBuilder();
        int i=0,j=0;
        while(i<a.length() && j<b.length()){
            if(a.charAt(i)!=b.charAt(j)){
                break;
            }
            ans.append(a.charAt(i));
            i++;
            j++;
        }
        return ans.toString();
    }
}