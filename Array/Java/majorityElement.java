import java.util.HashMap;


public class majorityElement {
    // HashMap approach   
    class SolutionHashMap {
        public int majorityElement(int[] nums) {
            if(nums.length < 2){
                return nums[0];
            }
            HashMap<Integer, Integer> hashMap = new HashMap<>();
            for(int i = 0; i <= nums.length; i++){
                if(hashMap.containsKey(nums[i])){
                    hashMap.put(nums[i], hashMap.get(nums[i]) + 1);
                    if(hashMap.get(nums[i]).intValue() > nums.length / 2){
                        return nums[i];
                    }
                }
                else{
                    hashMap.put(nums[i], 1);
                }
            }
            return -1;
        }
    }
    
    //Moore Voting appraoch
    class SolutionMoore{
        public int majorityElement(int[] nums) {
            int res = nums[0];
            int count = 1;
            for(int i = 1; i < nums.length; i++){
                if(count == 0){
                    res = nums[i];
                }
                if(res == nums[i]){
                    count += 1;
                }
                else if(res != nums[i]){
                    count -= 1;
                }
            }
        return res;
        }
    }
}
