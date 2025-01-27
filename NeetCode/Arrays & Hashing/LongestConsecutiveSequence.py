class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNums = set(nums)
        max_length = 0
        for num in distinctNums:
            i = 1
            while num + i in distinctNums:
                i += 1
            if i > max_length:
                max_length = i
        
        return max_length