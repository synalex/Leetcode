class Solution:
    '''
    Problem: find x in array
    Input: nums: List[int], x: int
    Output: index: int or -1 if no match 
    Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
    '''


    def search(self, nums: List[int], x: int) -> int:
        # define borders
        left = 0
        right = len(nums)-1
        # algorithm to check each border and srink them accoridngly
        while right >= left:
            mid = (left+right) // 2
            if nums[mid] > x:
                right = mid -1
            elif nums[mid] < x:
                left = mid+1
            elif nums[mid] in [x]:
                return mid
        return -1
