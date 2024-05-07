'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109

'''

from typing import List




import math

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        total_count = 0

        # The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

        for index, element in enumerate(nums):

            
            if element == k/2:
                total_count+=math.floor(nums.count(element)/2)
                nums = list(filter(lambda a: a != k/2, nums))

            
            else: 
                total_count += min(nums.count(element), nums.count(k-element))


            


        



        return total_count




print(Solution.maxOperations(Solution, [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))