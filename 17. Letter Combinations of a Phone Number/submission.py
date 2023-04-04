class Solution:
    def letterCombinations(self, digits):

        # create phone map to characters
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = []
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                output.append(currStr)
                return
            for char in phoneMap[digits[i]]:
                backtrack(i + 1, currStr + char)

        if digits:
            backtrack(0, '')
        return output