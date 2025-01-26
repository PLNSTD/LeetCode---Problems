class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        curr_product = 1

        for num in nums:
            curr_product = curr_product * num
            left_product.append(curr_product)

        curr_product = 1

        for idx in range(len(nums)-1, -1, -1):
            curr_product = curr_product * nums[idx]
            right_product.insert(0, curr_product)
        
        output = []

        for i in range(len(nums)):
            prec_index = i - 1 if i > 0 else -1
            next_index = i + 1 if i < len(nums) - 1 else len(nums)
            if prec_index != -1:
                if next_index != len(nums):
                    output.append(left_product[prec_index] * right_product[next_index])
                else:
                    output.append(left_product[prec_index])
            else:
                if next_index != len(nums):
                    output.append(right_product[next_index])
        
        return output