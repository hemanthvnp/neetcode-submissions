class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, n):
            x = nums[i]

            dp_max[i] = max(x, dp_max[i-1] * x, dp_min[i-1] * x)
            dp_min[i] = min(x, dp_max[i-1] * x, dp_min[i-1] * x)

        return max(dp_max)