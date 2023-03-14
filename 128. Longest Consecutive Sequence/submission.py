class Solution:
    def longestConsecutive(self, nums):
        
        '''
        Idea:
        We want to start checking for longest consecutive sequence from 'root/start' of a possible longest consecutive sequence.

        To do this, we want to traverse the entire array, and for each element nums[i] we will first check if there exists nums[i] - 1 in nums
        1. if there does, then that means that we are not at a possible start of the longest consecutive element. 
        2. else, we can do a dfs search to check if nums[i] + 1, nums[i] + 2 ... nums[i] + k, where k is the longest consecutive sequence length
        '''

        numsSet = set(nums)
        lcs = 0
        for num in nums:
            if num - 1 not in numsSet: 
                currNum = num
                currLength = 0
                while currNum in numsSet:
                    currNum += 1
                    currLength += 1
                lcs = max(lcs, currLength)
        return lcs
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''