class Solution:
    def fib(self, n: int) -> int:
        '''
        Problem: generate nth Fibonacci number.
        Input: n: int
        Output: int -> the nth Fibonacci number.
        Constraints: 0 <= n <= 30
        '''
        # recursive:
        ''' 
        if n == 0:
            return 0
        elif n == 1:
             return 1
        else:
             return self.fib(n-1) + self.fib(n-2)
        '''
        
        # recursive with memorization:
        ''' 
        cache = {0: 0, 1: 1}
        if n in cache:
            return cache[n]
        cache[n] = self.fib(n - 1) + self.fib(n - 2)  # Recursive case
        return cache[n]
        '''
        
        # iterative 
        # O(n) time, O(1) space
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
