class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }  

        for i in s:
            if i in mapping:
                if stack:
                    top = stack.pop()
                else:
                    top = "#"
                if mapping[i] != top:
                    valid = False
                    break
            else:
                stack.append(i)
        if len(stack) != 0:
            valid = False
        return valid
