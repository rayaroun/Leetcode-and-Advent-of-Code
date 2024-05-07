from collections import Counter

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        

        count_dict = Counter(nums)


        total_count = 0

        for key in count_dict.keys():
            
            

            if key == k/2:

                while(count_dict[key] >= 2):
                    count_dict[key]-=2
                    total_count+=1

            elif k-key in  count_dict.keys():
                while( count_dict[k - key] >= 1 and count_dict[key] >= 1 ):
                    count_dict[key] -= 1
                    count_dict[k - key] -= 1
                    total_count+=1
            
        
        return total_count
                    



        # The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

        # for key in in count_dict.key:

            
        #     if element == k/2:
        #         total_count+=math.floor(nums.count(element)/2)
        #         nums = list(filter(lambda a: a != k/2, nums))

            
        #     else: 
        #         total_count += min(nums.count(element), nums.count(k-element))


            


        




print(Solution.maxOperations(Solution,[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))