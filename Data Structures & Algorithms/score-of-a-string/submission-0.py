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
        i = 0
        temp = 0
        lst = []
        while i < len(s) - 1:
            ord(s[i]) # convert to ascii

            ablist = abs(ord(s[i]) - ord(s[i+1]))
            
            temp = temp + ablist
            print(temp)
            i = i + 1
        return temp

        