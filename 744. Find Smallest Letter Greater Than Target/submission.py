'''
Used binary search since it was sorted, hard part was figuring out when to search on the left and right side, be sure to think about example test cases because then it will become easier to understand.
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        noCharactersGreater = True
        smallestChar = 'z'
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (r + l) // 2
            # search on left
            if letters[mid] > target:
                noCharactersGreater = False
                r = mid - 1
                smallestChar = min(smallestChar, letters[mid])

            # search on right
            elif letters[mid] <= target:
                l = mid + 1


        if noCharactersGreater:
            return letters[0]
        else:
            return smallestChar
    

        '''
        Time complexity: O(logn)
        Space complexity: O(1)
        '''