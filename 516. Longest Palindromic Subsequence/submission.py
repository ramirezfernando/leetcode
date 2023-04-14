from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def LPS(l, r):
            # base cases
            if l > r:
                return 0
            if l == r:
                return 1
            # main
            if s[l] == s[r]:
                answer = 2 + LPS(l + 1, r - 1)
            else:
                answer = max(LPS(l + 1, r), LPS(l, r - 1))

            return answer

        return LPS(0, len(s) - 1)

'''
Time complexity: O(n^2)
Space complexity: O(n^2)
'''