class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        // String arr[] = s.split(" ");
        // return arr[arr.length-1].length();
        int n= s.length()-1;
        while(n>=0 && s.charAt(n)==' ') n--;
        int i=n;
        while(i>=0 && s.charAt(i)!=' ') i--;
        return s.substring(i+1,n+1).length();
    }
}