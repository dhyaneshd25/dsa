class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int i=0,j=s.length()-1;
        while(i<j){
            char l = s.charAt(i);
            char r = s.charAt(j);
           if(!((l>='a' && l<='z')||(l>='A' && l<='Z')||(l>='0' && l<='9'))){
                i++;
            }else if(!((r>='a' && r<='z')||(r>='A' && r<='Z')||(r>='0' && r<='9'))){
                j--;
            }else {
                char a = Character.toLowerCase(l);
                char b = Character.toLowerCase(r);
                if(a!=b) return false;
                i++;
                j--;
            }
    
            // while(i<j && i<s.length() && s.charAt(i)==' ') i++;
            // while(i<j && j>=0 && s.charAt(j)==' ') j--;

            // i++;
            // j--;
        }
        return true;
    }
}