'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.



'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        
        extracted_data = []
        extracted_indicies = []

        c1 = 0
        c2 = len(s)


        for i,j in enumerate(s):
            if j in ['a','e','i','o','u','A','E','I','O','U']:
                extracted_data.append(j)
                extracted_indicies.append(i)
        

        
        rev_counter = len(extracted_indicies)-1
        list_s = list(s)


        for data in extracted_data:

            list_s[extracted_indicies[rev_counter]] = data
            rev_counter -= 1
        

        return "".join(list_s)
        