class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        for i in range(len(s)):
            if s[i]=="[" or s[i]=="{" or s[i]=="(":
                k.append(s[i])
            if s[i]=="]":
                if not k:
                    return False
                if k[-1]!="[":
                    return False
                else:
                    k.pop()
            if s[i]=="}":
                if not k:
                    return False
                if k[-1]!="{":
                    return False
                else:
                    k.pop()
            if s[i]==")":
                if not k:
                    return False
                if k[-1]!="(":
                    return False
                else:
                    k.pop()
        if len(k)>0:
            return False
        else:
            return True