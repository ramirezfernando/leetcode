class Solution:
    def search(self, nums, target):

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r -= 1
            elif nums[mid] < target:
                l += 1
            else:
                return mid
        return -1