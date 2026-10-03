class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(numbers)):
            if target-numbers[i] not in s:
                s[numbers[i]] = i
            else:
                return [s[target-numbers[i]]+1,i+1]