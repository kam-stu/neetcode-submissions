class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {")": "(", "]" : "[", "}": "{"}

        for op in s:
            if op in close_map:
                if stack and stack[-1] == close_map[op]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(op)

        return len(stack) == 0

