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




# THIS APPROACH IS INEFFICIENT. ALTHOUGH IT IS WORKING FOR A FEW TEST CASES, IT'S RUNNING OUT OF TIME 

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        ops = 0 

        first = 0
        
        if len(nums) < 2:
            return 0
        else: 
            second = 1

        
        total_count = 0
        
        nums_len = len(nums)


        while first < nums_len:

            while second < nums_len:

                if (nums[first] + nums[second]) == k:
                    nums.pop(first)
                    nums.pop(second-1)
                    nums_len = len(nums)
                    total_count += 1
                    first = 0 


                    if len(nums) < 2:
                        return total_count
                    else: 
                        second = 1
                else:
                    second += 1

            first += 1
            if len(nums) < 2:
                return total_count
            else: 
                second = first + 1

        return total_count




print(Solution.maxOperations(Solution, [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))