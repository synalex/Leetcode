# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    '''
    Problem: in seq(1,2,...,n) find index i, if i is bad all i+n are bad-> find first bad i 
    Input: n: int
    Output: i: int
    Constraints: 1 <= bad <= n <= 231 - 1
    '''
    def firstBadVersion(self, n: int) -> int:
        ## we have defined borders, sorted monotone seq and its infinite
        ## we can use binSearch
        #define borders
        left = 1
        right = n
        bad = 0
        # algorithm to check each bad call and save the earliest            as possible bad call 
        while right >= left:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid -1
                bad = mid
            else:
                left = mid+1
        return bad 
Console

