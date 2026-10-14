import java.util.ArrayList;
import java.util.List;

class TextJustification {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<>();
       int n = words.length;
       int cl = 0, ci=0,c=0;
       int i=0;
       while(i<n){
            int nl = cl + words[i].length();
            if(nl>maxWidth){
                StringBuilder temp = new StringBuilder();
                int el = i-ci;
                int ts = maxWidth-(cl-el); 
                if(el-1==0){
                    temp.append(words[ci]);
                    temp.append(" ".repeat(ts));
                    ans.add(temp.toString());
                    cl = words[i].length()+1;
                    ci = i;
                    i++;
                }else{
                    int count = ts/(el-1);
                    if(ts%(el-1)==0){
                        StringBuilder temp2 = new StringBuilder();
                        for(int j=ci;j<=i-1;j++){
                            temp2.append(words[j]);
                            if(j!=i-1) temp2.append(" ".repeat(count));
                        }
                        ans.add(temp2.toString());
                        cl = words[i].length()+1;
                        ci = i;
                    i++;
                    }else{
                        int rem= ts%(el-1);
                        StringBuilder temp2 = new StringBuilder();
                        // temp2.append(words[ci]);
                        // temp2.append(" ".repeat(count+rem));
                        
                        
                        // ci++;
                        for(int j=ci;j<=i-1;j++){
                            temp2.append(words[j]);
                            if(j!=i-1) temp2.append(" ".repeat(count));
                            if(rem>0) {
                                temp2.append(" ");
                                rem--;
                            }
                        }
                        ans.add(temp2.toString());
                        cl = words[i].length()+1;
                        ci = i;
                        i++;
                    }
                    
                }
            }else if(nl==maxWidth){
                StringBuilder temp = new StringBuilder();
                for(int j=ci;j<=i;j++){
                    temp.append(words[j]);
                    if(j!=i) temp.append(' ');
                }
                ans.add(temp.toString());
                i++;
                cl=0;
                ci=i;
            }else{
                cl = nl;
                cl++;
                i++;
            }
       }
       if(cl>0){
            StringBuilder temp = new StringBuilder();
                int l = 0;
                for(int j=ci;j<n;j++){
                    temp.append(words[j]);
                    l+=words[j].length();
                    if(j!=n-1){
                     temp.append(" ");
                     l+=1;
                    }
                        
                }
                temp.append(" ".repeat(maxWidth-l));
                ans.add(temp.toString());
                 
       }
    return ans;
    }
}