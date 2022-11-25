class Solution:
    
    def climbStairs(self, n: int) -> int:
        '''
        Problem: Find all the possibilities of climbing stairs 
        Input: n: int
        Output: sum(possibility): n
        Constraints: 1 <= n <= 45
        '''
        # iterative
        # Time: O(n), Space: O(n)
        if n < 3:
            return n
        a, b = 1,2
        for _ in range(n-2):
            a, b = b, a+b
        return b
