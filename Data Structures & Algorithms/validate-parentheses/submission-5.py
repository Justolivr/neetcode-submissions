class Solution:
    def isValid(self, s: str) -> bool:
        """

        [ -> ] onto stack

        if  stacksize not even, then false

        push ( -> [ -> { -> } == { 180degrees

        key value
        {    }
        [    ]


        """
        i = 0
        stack = []
        dictionary = {"}": "{", ")": "(", "]": "["}
        if len(s) % 2 != 0: # if len(s) is odd, then is now 
            return False

        while i < len(s) :
            """ 
                when do i consider peeking?
                ( (([])) )
                (  ( ([]) )  )
                (  (  (  )    )  )  )
            """
   
            if s[i] in dictionary:  # if in dict as key
                if len(stack) == 0: # if length of stack is 0, then return False
                    return False
                peek = stack[-1]  # peek
                if dictionary[s[i]] == peek:
                    stack.pop()
                    # if value is has equ key, then pop
                else:
                    return False
            else:
                stack.append(s[i])  # append value to stack

            # if s[i] is in dict as a key, then peek, and check if corresponding value is the value pair,
           
            i += 1 # inc
        
        if not stack : # if there is a stack w values 
             return True

        return False
