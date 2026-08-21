class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Takes every character from the string, filters alpha numerical values, and returns a 
        # string. .lower() is to make it not case sensitive
        s = ''.join(filter(str.isalnum, s)).lower() 
        # compare original string to the reverse - using a slice, we can reverse the original 
        # string. 
        return s == s[::-1]
        