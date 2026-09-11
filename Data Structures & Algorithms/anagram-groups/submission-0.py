class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        try not to sort the strings, but could use a hashmap

        how anagrams work - has to be same length as other word, and has to have the same characters in
        both.
        (O(m*n)) -> must have inner loop and outer loop : m = no.strings, n = length of longest string

        must be grouped into sublists.
        output must have the same number as input -> there wont be 2 that are anagrams that share a 3rd 
        without including the other one. 

        any non- anagrams, should be displayed
        so we only make sublists if they are anagrams.

        we must need to use something like a dictionary.

        if we list all the items into a dictionary
        then for each item, we can search the dictionary for anytime the letter appears?

        for example,

        hat -> look for h, -> none, so retun "hat" as sublist
        cat -> look for words with c -> if we have it, note it down. then look for words that contain a.
            if temp value changes, then that word is not it.
            if we get to the end of the word, and there is a temp value/values that have it,
            append it onto the temp value and create that sublist.
        act
        pots
        tops
        stop

        so we only need a dictionary size of 26? for every letter


        '''

        d = {}


        for st in strs:
            sig = [0]*26
            for char in st:
                ind = ord(char) - ord('a')
                sig[ind] +=1
            key = tuple(sig)
            
            if key in d:
                d[key].append(st)
            else:
                d[key] = [st]
        return list(d.values())

        