'''


You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

 

Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

'''




class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        
        # max_avg  = (sum(nums[0:k]))/k
        print(nums[0:k])
        first_sum = sum(nums[0:k])
        max_sum = first_sum


        for i in range(1, len(nums)-k+1,1):
            # print(nums[i])
            print(nums[i])
            print(nums[i+k-1])
            first_sum = (first_sum-nums[i-1]+nums[i+k-1])

            # print("tmep sum " , temp_sum)

            if first_sum > max_sum:
                max_sum = first_sum


        # temp_sum = first_sum - nums[i+1] + nums[i+k]
        # if temp_sum > first_sum:
        #         first_sum = temp_sum

        return max_sum/k


        


print(Solution.findMaxAverage(Solution, [1,12,-5,-6,50,3], 4))



