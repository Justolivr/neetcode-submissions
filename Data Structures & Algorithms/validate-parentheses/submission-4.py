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
        if len(s) % 2 != 0 or len(s) == 1 :
            return False

        while i < len(s) :
            """ 
                when do i consider peeking?
                ( (([])) )
                (  ( ([]) )  )
                (  (  (  )    )  )           )


                then if
                a bracket is valid when it has a corresponding closing bracket
                (dictionary)
                if 
                [ [ [ ]
                      !
                dict(i) , then peek, then check if it maps to dict(i)

            """
    
            if s[i] in dictionary:  # if in dict as key
                if len(stack) == 0:
                    return False
                peek = stack[-1]  # peek
                if dictionary[s[i]] == peek:
                    stack.pop()
                    # if value is has equ key
                    # if peek.value is the value for key
                else:
                    return False
            else:
                stack.append(s[i])  # append value to stack

            # if s[i] is in dict as a key, then peek, and check if corresponding value is the value pair,
            # if it is,

            i += 1
            print(stack)
        
        if not stack : # if there is a stack w values 
             return True

        # for
        return False
