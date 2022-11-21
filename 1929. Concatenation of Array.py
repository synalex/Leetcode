class Solution:
    # return nums+nums would have been another solution LOL
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsout = nums
        for i in range (len(nums)):
            numsout.insert(len(numsout)+i, nums[i]) 
        return numsout
