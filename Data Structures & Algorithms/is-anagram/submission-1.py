class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashish = 26*[0]
        for i in range(len(s)):
            hashish[ord(s[i]) - ord('a')] = 1 + hashish[ord(s[i]) - ord('a')]
            hashish[ord(t[i]) - ord('a')] = hashish[ord(t[i]) - ord('a')] - 1
        return all(num == 0 for num in hashish)