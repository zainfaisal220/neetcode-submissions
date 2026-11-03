
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ans = dict()
        freq = dict()

        for i in range(len(s)):
            if s[i] in ans:
                ans[s[i]] += 1
            else:
                ans[s[i]] = 1

        for j in range(len(t)):
            if t[j] in freq:
                freq[t[j]] += 1
            else:
                freq[t[j]] = 1

        return ans == freq
