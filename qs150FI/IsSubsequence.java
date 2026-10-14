class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        if(s.length()>t.length()) return false;
        // int p=-1,c=0;
        // while(c<s.length()){
        //     boolean ck = false;
        //     for(int i=0;i<t.length();i++){
        //         if(c<s.length() && s.charAt(c)==t.charAt(i)){
        //             ck =true;
        //             if(p==-1){
        //                 p=i;
        //                 c++;
        //                 break;
        //             }else{
        //                 if(p>=i){
        //                     boolean ckk = false;
        //                     for(int j=p+1;j<t.length();j++){
        //                         if(s.charAt(c)==t.charAt(j)){
        //                             ckk = true;
        //                             p=j;
        //                             c++;
        //                             break;
        //                         }
        //                     }
        //                     if(!ckk) return false;
        //                 }else{
        //                     p=i;
        //                     c++;
        //                 }
        //             }
        //         }

        //     }
        //     if(!ck){
        //         return false;
        //     }
        // } 
        int in=-1;
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            int f = t.indexOf(ch,in+1);
            if(f<0) return false;
            in = f;
        }      
        return true;
    }
}