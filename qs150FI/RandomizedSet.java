import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

class RandomizedSet {
    List<Integer> arr;
    Map<Integer,Integer> st;
    Random r;
    public RandomizedSet() {
        st = new HashMap<>();
        arr = new ArrayList<>();
        r = new Random();
    }
    
    public boolean insert(int val) {
    if(st.containsKey(val)){
        return false;
    }else{
        arr.add(val);
        st.put(val,arr.size()-1);
        return true;
    }
    }
    
    public boolean remove(int val) {
    if(st.containsKey(val)){
         int index = st.get(val);
        arr.set(index, arr.get(arr.size() - 1));
        st.put(arr.get(index), index);
        arr.remove(arr.size() - 1);
        st.remove(val);
        return true;
    }else{
        return false;
    }
    }
    
    public int getRandom() {
       int ind = r.nextInt(arr.size());
        return arr.get(ind);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */