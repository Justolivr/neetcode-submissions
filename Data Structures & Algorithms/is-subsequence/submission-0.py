class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0 # pointer1
        j = 0 # pointer2

        while i < len(s) and j < len(t):
            if s[i] == t[j]: # if chars match, advance i to look for next char of s
                i = i + 1 # increment i if matched
            j = j + 1 # increment j no matter what
        return i == len(s) # return bool 