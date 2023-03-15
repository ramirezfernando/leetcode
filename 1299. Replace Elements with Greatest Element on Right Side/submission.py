class Solution:
    def replaceElements(self, arr):

        # start from right to left
        currMax = - 1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], currMax = currMax, max(currMax, arr[i])
        return arr