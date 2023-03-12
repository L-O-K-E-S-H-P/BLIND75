'''You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
Input: words = ["are","amy","u"], left = 0, right = 2
Output: 2
Explanation: 
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.

 '''
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels=set(['a','e','i','o','u'])
        count=0
        
        for i in range(left,right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count=count+1
        return count
            
        
