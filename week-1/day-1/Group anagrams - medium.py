class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            r = "".join(sorted(s))
            if r in res.keys():
                res[r].append(s)
            else:
                res.update({r:[s]})
        return res.values()

        
