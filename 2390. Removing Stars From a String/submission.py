class Solution:
    def removeStars(self, s):

        stack = []

        for char in s:
            if char == '*' and stack:
                stack.pop()
            else:
                stack.append(char)

        output = ""
        for char in stack:
            output += char
        return output