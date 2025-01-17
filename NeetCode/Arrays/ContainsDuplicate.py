class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        occ_map = {}

        for idx in range(0, len(nums)):
            if occ_map.get(nums[idx], False):
                return True
            occ_map[nums[idx]] = True
        
        return False