class ReverseWords {
    public String reverseWords(String s) {
        StringBuilder ans = new StringBuilder();
        int j = s.length()-1;
        while(j>=0){
            char ch = s.charAt(j);
            if(ch==' '){
                j--;
            }else{
                int i=j;
                while(i>=0 && s.charAt(i)!=' ') i--;
                ans.append(s.substring(i+1,j+1));
                ans.append(' ');
                j=i;
            }
        }
        String res = ans.toString();
        if(res.charAt(res.length()-1)==' '){
            return res.substring(0,res.length()-1);
        }
        return ans.toString();
    }
}