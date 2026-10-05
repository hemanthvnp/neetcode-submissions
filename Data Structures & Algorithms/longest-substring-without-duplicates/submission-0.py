class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        maxl = 0
        k = {}
        if len(s)==0:
            return 0
        while left<len(s) and right<len(s):
            if s[right] not in k:
                k[s[right]] = 1
                l = right - left + 1
                maxl = max(maxl,l)
                right+=1
            else:
                k.pop(s[left])
                left+=1
        return maxl