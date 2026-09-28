class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            if nums[i] not in result:
                if (target - nums[i]) in result:
                    return [result[target - nums[i]], i]
                result[nums[i]] = i
            else:
                if (target - nums[i]) in result:
                    return [result[target - nums[i]], i]
        