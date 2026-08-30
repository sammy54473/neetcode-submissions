class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            hashish = 26*[0]
            for i in s:
                hashish[ord(i) - ord('a')] = 1 + hashish[ord(i) - ord('a')]
            res[tuple(hashish)].append(s)
        return list(res.values())