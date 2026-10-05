class Solution(object):
    def minWindow(self, s, t):

        if len(t) > len(s):
            return ""

        t_freq = {}
        window = {}

        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        have = 0
        need = len(t_freq)

        left = 0
        res_len = float("inf")
        res_left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in t_freq and window[ch] == t_freq[ch]:
                have += 1

            while have == need:

                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res_left = left

                left_char = s[left]

                if left_char in t_freq and window[left_char] == t_freq[left_char]:
                    have -= 1

                window[left_char] -= 1
                left += 1

        if res_len == float("inf"):
            return ""

        return s[res_left:res_left + res_len]