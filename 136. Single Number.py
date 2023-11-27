#class Solution(object):
def singleNumber(nums: list):
        """
        Given a non-empty array of integers nums, every            elementappears   
        twice except for one. Find that single one.    
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i, num in enumerate(nums):
            if i == 0 and num != nums[i+1]:
                return num
            elif i == len(nums)-1 and num != nums[len(nums)-2]:
                return num
            if num != nums[i-1] and num != nums[i+1]:
                return num

            
            
singleNumber([1,1,4])
                

            



        