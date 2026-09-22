class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        counts = {}
        lst = []
        
        while i < len(nums):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] = counts[nums[i]] + 1
            i += 1
        
        r = 0
        while r < k:
            bcount = -1
            bkey = None
            for key in counts:
                if key not in lst:
                    if counts[key] > bcount:
                        bkey = key
                        bcount = counts[key]
            lst.append(bkey)
            r +=1
        return lst


    # Really horrible Complexity.