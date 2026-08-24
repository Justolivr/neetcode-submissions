class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)): # loop through all of the values
            max_val = -1 # define max val as -1 - so we dont need to define it when we have no value.
            for j in range(i +1 , len(arr)):
                if arr[j] > max_val: # if number is bigger, then change max_val
                    max_val = arr[j]
            arr[i] = max_val # if number is smaller, then change arr[i] value
                    
            
        return arr
  
  # O complexity = O(N)
  