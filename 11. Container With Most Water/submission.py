class Solution:
    def maxArea(self, height):
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''