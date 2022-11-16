class Solution:
    def isValid(self, s: str) -> bool:
        # no input
        if len(s) == 0:
            return True
        stack = []
        for char in s:
            # open paranthesis
            if char == "(" or char == "[" or char == "{":
                    stack.append(char)
                    pass
            if char == ")" or char == "]" or char == "}":
                # can't start with a close one
                if len(stack) == 0:
                    return False 
                elif char == ")":
                    temp = stack.pop()
                    if temp != "(":
                        return False
                elif char == "]":
                    temp = stack.pop()
                    if temp != "[":
                        return False
                elif char == "}":
                    temp = stack.pop()
                    if temp != "{":
                        return False    
        if len(stack) == 0:
            return True
        # if not finished
        else:
            return False
                
            
