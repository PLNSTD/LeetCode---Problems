class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementary_hash = {}

        for idx, num in enumerate(nums):
            if complementary_hash.get(target-num, False) is not False:
                return [complementary_hash[target-num], idx]
            complementary_hash[num] = idx
        
        return [0,1]