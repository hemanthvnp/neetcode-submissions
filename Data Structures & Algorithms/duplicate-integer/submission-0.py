class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate[nums[i]] = 1
            else:
                return True
        return False
        