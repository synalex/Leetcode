# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Time complexity : O(log2(n))
        Space complexity : O(1)
        """
        left = 1
        right = n       
        while right >= left:
            mid = (left + right) // 2
            i = guess(mid)
            if i == 1:             
                left = mid + 1     
            elif i == -1:
                right = mid - 1
            elif i == 0:
                return mid
            else:
                print("bug")
