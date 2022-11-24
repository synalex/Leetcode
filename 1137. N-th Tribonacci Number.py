class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        Problem: find N-th Tribunacci Number
        Input: n: int
        Output: Tn : int
        Constraints: 0 <= n <= 37
        '''
        # recursive
        # Time: O(n), Space: 0(n)
        # https://docs.python.org/3/library/functools.html#functools.lru_cache
        '''
        @lru_cache(maxsize=None)
        if n < 1:
			return 0
		if n < 3:
			return 1
		return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        '''
        #iterative
        # Time: O(n), Space: 0(1)
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c, = b, c, a+b+c
        return a
