class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        def backtrack(open,close):
            nonlocal path
            if open==n and close==n:
                res.append(path)
                return
            if open<n:
                path+="("
                backtrack(open+1,close)
                path = path[:-1]
            if close<open:
                path+=")"
                backtrack(open,close+1)
                path = path[:-1]
        backtrack(0,0)
        return res
