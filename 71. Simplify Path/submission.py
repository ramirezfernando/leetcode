class Solution:

    def simplifyPath(self, path: str) -> str:
        # ex: /home
        def getPath(i):
            currPath = "/"
            count = i + 1
            while count < len(path) and path[count] != '/':
                currPath += path[count]
                count += 1
            return currPath

        stack = []
        for i in range(len(path)):
            if path[i] == '/':
                currPath = getPath(i)
                if stack and currPath == '/..':
                    stack.pop()
                elif currPath != '/.' and currPath != '/' and currPath != '/..':
                    stack.append(currPath)

        if not stack:
            return '/'
        return "".join(stack)