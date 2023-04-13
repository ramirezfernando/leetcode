'''
Pretty simple problem
'''
class Solution:
    def twoSum(self, numbers, target):

        l, r = 0, len(numbers) - 1
        while l < r:
            numSum = numbers[l] + numbers[r]
            if numSum < target:
                l += 1
            elif numSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]