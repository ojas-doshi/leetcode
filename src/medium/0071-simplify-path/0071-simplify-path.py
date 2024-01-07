class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for comp in components:
            if comp == '..':
                if stack:
                    stack.pop()
            elif comp and comp != '.':
                stack.append(comp)

        return '/' + '/'.join(stack)
