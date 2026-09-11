class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        string matching in an array:

        contiguous, non-empty sequence of characters.
        can be a substring of any word.
        has to be > 2 characters - shown by example 3.
        so one example

        mass, as, hero, superhero

        so as is substring of mass, hero substring of superhero.

        so would i need to pick maybe the 2 smallest length strings, and have them be comparisons.
        i was thinking this because you would only need to match everything with them with the smallest 
        lengths.
        they have to be whole words, so the entire string needs to match with every other.
        but if you did it brute force, then it would take so long

    
        but how would I implement this?
        sort the list from smallest to biggest:
        as, mass, hero, superhero
        take the first one, and compare with the others:
        maybe you could make a dictionary:


        where the keys are the 2 smallest values (as, hero)
        and the values are matches with them values (mass, superhero)
        '''

 

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res