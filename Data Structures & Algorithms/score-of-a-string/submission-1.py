class Solution:
    def scoreOfString(self, s: str) -> int:
        

        '''
        c = 99    
        o = 111
        d = 100
        e = 101 

        so bigger value goes left: |111 - 99| +

        needs to take 2 values (so i, j)

        take 2, convert to ascii. - use 'ord'

        so |111-99| == abs(i - j)
        need a for loop to add abs

        '''
        i = 0 # loop counter
        temp = 0 # temp value to add total
        while i < len(s) - 1:
            ablist = abs(ord(s[i]) - ord(s[i+1])) # define absolute values of each pair
            temp = temp + ablist # add to temp for a running total
            i = i + 1 # inc
        return temp

        