class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        res=0
        for i in range(n):
            checked = [0]*256
            for j in range(i,n):
                if(checked[ord(s[j])]==True):
                    break
                else:
                    res=max(res,j-i+1)
                    checked[ord(s[j])] = True
            checked[ord(s[j])] = False
        return res