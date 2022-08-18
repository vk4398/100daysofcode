class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=s[0]
        resLen=0
        res_l=0
        res_r=0
        for i in range(len(s)):
            l,r=i-1,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>resLen):
                    resLen=r-l+1
                    res_l=l
                    res_r=r
                l-=1
                r+=1
            
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>resLen):
                    resLen=r-l+1
                    res_l=l
                    res_r=r
                l-=1
                r+=1
        res=s[res_l:res_r+1]
        return res
            