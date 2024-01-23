# [p01] 유효한 팰린드롬
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
        
print(Solution().isPalindrome("Hello, this is ME"))
