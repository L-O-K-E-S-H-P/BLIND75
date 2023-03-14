class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=str(x)[::-1]
        if(c==str(x)):
            return True
        else:
            return False
