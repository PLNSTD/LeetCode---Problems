class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occ_str = {}

        for char in s:
            occ_str[char] = occ_str.get(char, 0) + 1
        
        for char in t:
            occ_str[char] = occ_str.get(char, 0) - 1
            if occ_str[char] == -1:
                return False
        
        return True