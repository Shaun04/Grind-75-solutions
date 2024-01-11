import java.util.HashMap;

public class TwoSums{
    // Brute force approach
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            for(int i = 0; i < nums.length; i++){
                int temp = target - nums[i];
                for(int j = i+1; j < nums.length; j++){
                    if(nums[j] == temp){
                        return new int[] {i,j};
                    }
                }
            }
            return new int[] {};
        }
    }
    
    // Hashmap approach
    class SolutionHashMap {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> hashMap = new HashMap<>();
            for(int i =0; i < nums.length; i++){
                int leftover = target - nums[i];
                if(hashMap.containsKey(leftover)){
                    return new int[] {hashMap.get(leftover), i};
                }
                hashMap.put(nums[i], i);
            }
            return new int[] {};
            
        }
    }
}


