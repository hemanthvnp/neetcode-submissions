class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 0
        maxprofit = 0
        while left<len(prices) and right<len(prices):
            if prices[right]>prices[left]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit,profit)
                right+=1
            else:
                left=right
                right+=1
        return maxprofit