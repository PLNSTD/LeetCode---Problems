## Problem: 1768. Merge Strings Alternately
## Problem Link: https://leetcode.com/problems/merge-strings-alternately

class Solution(object):
    def mergeAlternately(self, word1, word2):
        idx = 0
        merged = ''
        while idx < len(word1) and idx < len(word2):
            merged += word1[idx]
            merged += word2[idx]
            idx += 1
        
        if idx < len(word1):
            merged += word1[idx:]
        if idx < len(word2):
            merged += word2[idx:]
        
        return merged