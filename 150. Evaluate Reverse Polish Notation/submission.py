class Solution:
    def evalRPN(self, tokens):

        stack = []
        for token in tokens:

            if token == '+':
                left_token = stack.pop()
                right_token = stack.pop()
                stack.append(right_token + left_token)

            elif token == '-':
                left_token = stack.pop()
                right_token = stack.pop()
                stack.append(right_token - left_token)

            elif token == '*':
                left_token = stack.pop()
                right_token = stack.pop()
                stack.append(right_token * left_token)


            elif token == '/':
                left_token = stack.pop()
                right_token = stack.pop()
                stack.append(int(right_token / left_token)) # division between two integers always truncates toward zero.

            else:
                stack.append(int(token))
                
        return stack[0]