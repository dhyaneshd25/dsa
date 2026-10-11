import java.util.HashMap;
import java.util.Map;

class RomanToInt {
    public int romanToInt(String s) {
        Map<Character,Integer> mp = new HashMap<>();
        mp.put('I',1);
        mp.put('V',5);
        mp.put('X',10);
        mp.put('L',50);
        mp.put('C',100);
        mp.put('D',500);
        mp.put('M',1000);
        int ans = 0;
        int i = s.length()-1;
        while(i>=0){
            char ch = s.charAt(i);
            ans+=mp.get(ch);
            if(i-1>=0){
                char pc = s.charAt(i-1);
                if((ch=='V' || ch=='X') && pc=='I'){
                    ans -=1;
                    i--;
                }else if((ch=='L' || ch=='C') && pc=='X'){
                    ans -=10;
                    i--;
                }else if((ch=='D' || ch=='M') && pc=='C'){
                    ans -=100;
                    i--;
                }
            }
            i--;
        }
        return ans;
    }   
}