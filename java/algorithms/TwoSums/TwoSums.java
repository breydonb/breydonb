import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSums {
    public static void main(String[] args){
        int[] array = {3,1};
        int target = 4;
        System.out.println(Arrays.toString(twoSum(array, target)));
    }
    
    public static int[] twoSum(int[] array, int target){
        /* 
            We use a hash map to store the element as the key and the index as the value. 
            The reason we use a hash map is to get at worse a O(n) time complexity and at best O(1)
        */
        Map<Integer,Integer> hashMap = new HashMap<Integer,Integer>();
        
        for(int i = 0; i < array.length; i++){
            int diff = target - array[i];
            if(hashMap.containsKey(diff)){
                // We return the values for the key diff, then the current index we are at
                return new int[] {hashMap.get(diff),i};
            }
            else{
                // If the difference variable isn't a key, we can go ahead and add the initial element along with the index
                hashMap.put(array[i],i);
            }
        }
        // If there are no values that add up to target, we should return null
        return null;
    }
}
