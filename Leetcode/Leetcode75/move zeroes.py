'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


'''
class Solution:
    def moveZeroes(self, nums) -> None:

        i = 0
        j = i
        while i <= len(nums)-1  and i <= j:

            if nums[i]==0:
                while nums[j] == 0:
                    if  j < len(nums)-1:
                        j+=1
                    else:
                        break

                # x, y = y, x
                nums[i],nums[j] = nums[j],nums[i]
                i+=1

            else:
                i+=1
                j+=1
