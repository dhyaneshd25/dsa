import java.util.HashMap;

class IntToRoman {

    public String intToRoman(int num) {
        HashMap<Integer,String> mp = new HashMap<>();
        mp.put(1,"I");
        mp.put(2,"II");
        mp.put(3,"III");
        mp.put(4,"IV");
        mp.put(5,"V");
        mp.put(6,"VI");
        mp.put(7,"VII");
        mp.put(8,"VIII");
        mp.put(9,"IX");
    
        StringBuilder ans = new StringBuilder();
        int m = num/1000;
        if(m>0){
            ans.append("M".repeat(m));
            num -= m*1000;
        }
        m = num/900;
        if(m == 1){
            ans.append("CM");
            num -=900;
        }
        m = num/500;
        if(m==1){
            ans.append("D");
            num-=500;
        }
        m = num/400;
        if(m==1){
            ans.append("CD");
            num-=400;
        }
        m = num/100;
        if(m>0){
            ans.append("C".repeat(m));
            num -= 100*m;
        }
        m = num/90;
        if(m==1){
            ans.append("XC");
            num -= 90;
        }
        m =  num/50;
        if(m==1){
            ans.append("L");
            num -=50;
        }
        m = num/40;
        if(m==1){
            ans.append("XL");
            num -= 40;
        }
        m = num/10;
        if(m>0){
            ans.append("X".repeat(m));
            num -=m*10;
        }
        if(num>0) ans.append(mp.get(num));
 

        return ans.toString();
    }
}