class Solution:
    def countSeniors(self, details: List[str]) -> int:

        p = 0 # no. passengers

        for d in details: # for each details
            age = int(d[11:13]) # age is 12th and 13th char
            if age > 60: # if age >60, add passengers.
                p +=1
                
        return p
        