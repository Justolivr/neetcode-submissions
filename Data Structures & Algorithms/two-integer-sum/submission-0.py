class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # define dictionary
        indices = [] # define return var
        temp = 0 # define temp 
        for i in range(len(nums)): 
            temp = target - nums[i] # find complement of each value in nums
            if temp not in dictionary: 
                dictionary.update({nums[i]: i}) # add each value to dictionary if it hasn't been added
                
            else:
                # if a key of one pair equals a value of another pair, we can say that they both add up to the target number
                indices.append(dictionary[temp]) # append value from dictionary in earlier index
                indices.append(i) # append value from dictionary in current index
       
        return indices       