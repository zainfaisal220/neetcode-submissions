class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        i=0
        max_area=0
        for j in range (len(s)):
            while s[j] in window :
                window.remove(s[i])
                i+=1
            window.add(s[j])
            max_area=max(max_area,j-i+1)
        return max_area    

        