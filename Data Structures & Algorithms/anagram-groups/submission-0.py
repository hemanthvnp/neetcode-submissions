class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==1 :
            return[strs]
        d={}
        for i in strs:
            k=str(sorted(i))
            if k in d:
                d[k].append(i)
            else:
                d[k]=[i]
        return list(d.values())        