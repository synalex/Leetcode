class Solution:
    '''
    Problem: reverse integer
    inpit: int: x
    output: int: x if abs(x) > 2**31-1 return 0
    constraints: -231 <= x <= 231 - 1
    '''
    def reverse(self, x: int) -> int:
            # Initialzize variables
            x=str(x)
            stack = []

            # stack it up
            for digit in x:
                stack.append(digit)

            # check for negative sign
            if x[0] not in ["-"]:
                x=""
            else:
                x="-"
    
            # stack it back
            for i in range(len(stack)):
                x+=stack.pop()

            # check if it was negative     
            if x[-1] in ["-"]:
                x = "".join(x[:-1]) 
            else: 
                pass 

            # return to int
            x = int(x)

            # check if in the integral
            if abs(x) <= 2**31-1:
                return x
            else:
                return 0
