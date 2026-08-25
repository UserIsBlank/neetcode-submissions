class Solution:
    def isValid(self, s: str) -> bool:
        # []{}
        # stack = [[,{]
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            # Check if matching close bracket exists
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # Add char to stack if open bracket
            else:
                stack.append(c)
        
        # Return true if stack is empty
        return True if not stack else False