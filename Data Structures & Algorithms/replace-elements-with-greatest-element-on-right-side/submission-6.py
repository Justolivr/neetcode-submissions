class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1 # define max value from the right

        for i in range(len(arr) - 1, -1, -1): 
            current = arr[i] # make  value into the value of current index
            arr[i] = max_right # assign max_right to current array index
            max_right = max(max_right, current) # use max function to compare both

        return arr

# O complexity - O(N)