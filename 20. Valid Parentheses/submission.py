class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif (stack and ((stack[-1] == '(' and char == ')') 
                        or (stack[-1] == '{' and char == '}') 
                        or (stack[-1] == '[' and char == ']'))):
                        stack.pop()
            else:
                return False
        
        if stack:
            return False
        return True
        '''
        Time: O(n)
        Space: O(n)
        '''