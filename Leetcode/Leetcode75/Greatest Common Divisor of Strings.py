'''

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.



'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        len1 = len(str1)
        len2 = len(str2)

        shorter_len = len1 if len1<len2 else len2
        shorter_str = str1 if len1<len2 else str2

        divisible_lens = []


        for i in range(shorter_len,0,-1):
            if (len1 % i == 0 ) and (len2 % i == 0 ):
                divisible_lens.append([i,int(len1/i),int(len2/i)])


        for j in divisible_lens:
            if shorter_str[:j[0]]*j[1] == str1 and shorter_str[:j[0]]*j[2] == str2:
                return (shorter_str[:j[0]])

        return ""