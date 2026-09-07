class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0 # pointer
        count = 0
        '''
        need to print last word
        need to exclude spaces in the word

        so if there is a space before a character, then the next char should be a start of a word.
        or, we could traverse backwards from the end of the string, then use a pointer to traverse until
        we hit a letter - then increment a count for every time we move left, and we have a letter.
        when we hit a space again, then end the loop.

        so _ -> first condition
           a... -> second condition
           _-> third condition

           so _ (aaaa) _


        '''

        for i in range(len(s)-1,-1, -1):
            # if space, then move left until you hit a letter

            if ' ' in s[i]:
                continue
            else:
                count +=1
                if ' ' in s[i-1]:
                    break

        return count