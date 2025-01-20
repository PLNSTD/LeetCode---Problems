class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagram_groups = {}

        for string in strs:
            occ_map = [0] * 26
            for char in string.lower():
                occ_map[ord(char)-97] += 1
            occ_map = tuple(occ_map)
            if anagram_groups.get(occ_map, False) is not False:
                anagram_groups.get(occ_map).append(string)
            else:
                anagram_groups[occ_map] = [string]

        
        for group in anagram_groups:
            output.append(anagram_groups[group])


        return output