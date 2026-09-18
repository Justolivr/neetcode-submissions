class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        mprof = 0 # max profit
        prof = 0 # profit of current prices
        low = prices[0] # define as first index,
        
        while i < len(prices) - 1:

            if prices[i] < low:
                low = prices[i]

            prof = prices[i + 1] - low
            if prof > mprof:
                mprof = prof
            
            i +=1
        return mprof
