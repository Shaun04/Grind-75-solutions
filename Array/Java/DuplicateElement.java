import java.util.HashSet;
import java.util.HashMap;

public class DuplicateElement {
    //using Hashset
    class SolutionSet {
        public boolean containsDuplicate(int[] nums) {
            HashSet<Integer> seen = new HashSet<>();
            for(int num:nums){
                if(seen.contains(num)){
                    return true;
                }
                seen.add(num);
    
            }
            return false;
        }
    }

    //Using Hashmap
    class SolutionMap {
        public boolean containsDuplicate(int[] nums) {
            HashMap<Integer, Integer> hashMap = new HashMap<>();
            for(int num:nums){
                if(!hashMap.containsKey(num)){
                    hashMap.put(num, 1);
                }
                else{
                    return true;
                }
            }
            return false;
        }
    }
}
