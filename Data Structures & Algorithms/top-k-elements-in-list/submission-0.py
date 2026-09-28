class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        l = []

        for r in sorted_dict:
            if len(l) == k:
                break
            l.append(r)

        return l