class Solution:
    def productExceptSelf(self, nums):

        '''
        [1,2,3,4]

        prefix =   1, [ 1,  2,  6, 24]
        postfix = [24, 24, 12, 4] 1

        output = [24, 12, 8, 6]
        '''

        prefix = []
        prefix.append(1)
        currProd = 1
        for num in nums:
            currProd *= num
            prefix.append(currProd)
        print(prefix)
        
        postfix = [0] * len(nums)
        currProd = 1
        i = len(nums) - 1
        for num in nums[::-1]:
            currProd *= num
            postfix[i] = currProd
            i -= 1
        postfix.append(1)
        print(postfix)

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i + 1])
        return output