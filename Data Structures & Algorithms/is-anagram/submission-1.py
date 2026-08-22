class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # if they arent the same length, then they arent a anagram.
            return False
        dictionary = {} # define dictionary

        for sstr in s: # first loop : add key value pairs in dictionary to count no. occurences of each char in the word.
            if sstr in dictionary:
                dictionary[sstr] = dictionary[sstr] + 1 # if in dict already, increment
            else:
                dictionary[sstr] = 1 

        for tstr in t: # second loop : compare each character with other string. If already in dict, remove 1 value. 
            if tstr in dictionary:
                dictionary[tstr] = dictionary[tstr] - 1
            else:
                return False

        for count in dictionary.values(): # count every occurence of characters left - if they all show 0 then anagram is true.
            if count != 0:
                return False
            
        return True