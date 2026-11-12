class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def palindrome(s):
            return s==s[::-1]
        def backtrack(i):
            if i==len(s):
                res.append(path[:])
                return
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                if palindrome(sub):
                    path.append(sub)
                    backtrack(j)
                    path.pop()
        backtrack(0)
        return res