class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i = 0 # loop counter
        temp = 0 # temp value to add total
        while i < len(s) - 1:
            ablist = abs(ord(s[i]) - ord(s[i+1])) # define absolute values of each pair
            temp = temp + ablist # add to temp for a running total
            i = i + 1 # inc
        return temp

        