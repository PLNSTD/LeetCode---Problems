class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ_map = {}
        
        for num in nums:
            occ_map[num] = occ_map.get(num, 0) + 1

        top_k_keys = [key[0] for key in sorted(occ_map.items(), key=lambda item: item[1], reverse=True)[:k]]

        return top_k_keys
