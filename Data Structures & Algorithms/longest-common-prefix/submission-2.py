class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        longest common prefix:

        define a value that stores the first str in the list
        this is because we might want to assume that the whole word could be a LCP

        then, we must compare that value with every other string in the list

        so for example,

        pref = "bat"
        then, say for example if the second string is bag:

        have 2 pointers - one i, one j.
        if i is equal to j, then we can increment both AND append letter "b" into a temp value
        try again, if a = a, then append a to list, so we have "ba".

        example:

        bat, bag, beg

        strs[0] = bat

        compare strs[0][0] with strs[0 + 1][0] 
        "b", "b" - true
        then, increment so we compare strs[0][0] with strs[2][0]
        "b", "b" - true
        when we've reached the end, append "b" to prefix:
        increment strs[0][1], and compare strs[1][1]
        "a", "a", move to strs[2][1] - rename last bracket to i
        then, if we get to a point where we dont equal, then that's the max, doesn't matter what the other 
        ones are.
        so return  

        once we reach a point where both don't match, that means we have reached the max common prefix for 
        this.

        but what happens if the next one is smaller e.g. beg?
        well, this would be caught, because we get to a point where a = e, and then we exit the loop


        '''
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
    