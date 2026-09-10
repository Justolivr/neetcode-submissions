class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        pref = strs[0] # init first value

        for st in strs[1::]: # compare with rest of values
            i = 0 
            while i < len(pref) and i < len(st): # if one is shorter, then we can only compare length
                if pref[i] == st[i]: # if the same, inc
                    i += 1
                else:
                    break
            pref = pref[:i] # show number values before i

                
        return pref
    