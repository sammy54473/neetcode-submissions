class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        best = left = 0
        for r in range(len(s)):
            if s[r] in mp:
                left = max(mp[s[r]]+1, left)
            mp[s[r]] = r
            best = max(best,r-left+1)
        return best