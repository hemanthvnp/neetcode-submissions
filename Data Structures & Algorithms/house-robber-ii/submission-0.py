class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n-1):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        ans1 = max(dp[n-1],dp[n-2])
        dp[0] = 0
        for i in range(1,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        ans2 = max(dp[n-1],dp[n-2])
        return max(ans1,ans2)