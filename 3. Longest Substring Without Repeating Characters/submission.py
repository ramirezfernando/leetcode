'''
Pretty easy sliding window, when window has duplicate letters, shrink window from the left until it doesn't have duplicate values
'''
class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) == 1:
            return 1
    
        longestSubstring = 0
        visited = set()
        l = 0
        for r in range(len(s)):
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
            longestSubstring = max(longestSubstring, r - l + 1)
            visited.add(s[r])
        return longestSubstring