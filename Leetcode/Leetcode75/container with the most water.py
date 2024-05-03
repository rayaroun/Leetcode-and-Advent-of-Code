'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1



'''

class Solution:
    def maxArea(self, heights) -> int:

        left, right = 0, len(heights)-1
        area = 0 

        while left < right:
            
            if ((heights[left] if heights[left]<heights[right] else heights[right]) * (right-left)) > area:
                area = (heights[left] if heights[left]<heights[right] else heights[right]) * (right-left)

                if heights[left] < heights[right]:
                    left +=1
                else:
                    right -=1
            else:
                if heights[left] < heights[right]:
                    left +=1
                else:
                    right -=1

            
        return area





''' 
first, second = float('-inf'), float('-inf')
area = 0
first_wall, second_wall = 0, 0 

for index,wall in  enumerate(heights):

    if wall > first:

        first, second = second, first
        first_wall, second_wall = second_wall, first_wall
        first = wall
        first_wall = index
        area = ((index-first_wall)*(wall if wall < first else first)) if ((index-first_wall)*(wall if wall < first else first)) > ((index-second_wall)*(wall if wall < second else second)) else ((index-second_wall)*(wall if wall < second else second))

    elif wall > second:

        second = wall 
        second_wall = index
    



    elif ((index-first_wall)*(wall if wall < first else first)) > area or ((index-second_wall)*(wall if wall < second else second)) > area :
        area = ((index-first_wall)*(wall if wall < first else first)) if ((index-first_wall)*(wall if wall < first else first)) > ((index-second_wall)*(wall if wall < second else second)) else ((index-second_wall)*(wall if wall < second else second))
        # second = wall
        # second_wall = index



area = ((index-first_wall)*(wall if wall < first else first)) if ((index-first_wall)*(wall if wall < first else first)) > ((index-second_wall)*(wall if wall < second else second)) else ((index-second_wall)*(wall if wall < second else second))

return area
'''


print(Solution.maxArea(Solution,heights=[1,2,4,3]))
