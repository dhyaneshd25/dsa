class IndexOfFirstOccurenceString {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(),m = needle.length();
        if(m>n) return -1;
        for(int i=0;i<n-m+1;i++){
            String temp = haystack.substring(i,i+m);
            if(temp.equals(needle)){
                return i;
            }
        }
        return -1;
        // return haystack.indexOf(needle);
    }
}