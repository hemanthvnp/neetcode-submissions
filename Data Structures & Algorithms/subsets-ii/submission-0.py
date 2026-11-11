class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        nums.sort()
        def backtrack(i,path):
            if i==len(nums):
                if path not in res:
                    res.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()

            backtrack(i+1,path)
        backtrack(0,path)
        return res