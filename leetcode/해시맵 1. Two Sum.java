class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            if (map.containsKey(target - cur)) {
                int[] ret = {map.get(target - cur), i};
                return ret;
            }
            map.put(cur, i);
        }
        return null;
    }
}