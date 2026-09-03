class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0 # pointer1
        j = 0 # pointer2
        count = 0
        while i < len(s) and j < len(t): 
            if s[i] == t[j]: # compare values, if correct move both pointers forward
                i = i + 1
                j = j + 1
            else:
                i = i + 1 # move only pointer 1, as we nee
        count = len(t) - j
        return count

        