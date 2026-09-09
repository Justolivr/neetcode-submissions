class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''

        consec 1s

        if 2 ones, then a 0
        count 1,s until it gets to 0, then store as max count, and reset to 0
        '''
        temp = 0 # temp val
        maxc = 0 # max count
        for num in nums:
            if num == 1: # if 1
                temp += 1 #incr temp 
            else: 
                temp = 0 # reset temp val to 0
            if temp >= maxc: # if we get a temp value bigger than maxc, then update maxc
                maxc = temp
            print (maxc, temp)                       
        return maxc