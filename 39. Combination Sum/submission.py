class Solution:
    def combinationSum(self, candidates, target):

        answer = []
        # index: used to make sure we don't generate permutations
        # currSum: current sum
        # currList: current list
        def backtrack(index, currSum, currList):

            if currSum == target:
                answer.append(currList)
                return
            if currSum > target:
                return
            for i in range(index, len(candidates)):
                backtrack(i, currSum + candidates[i], currList + [candidates[i]])

        backtrack(0, 0, [])
        return answer