class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        sign=1
        n=2**31
        i=0
        while i<len(s):
            if(s[i]==" "):
                i+=1
            else:
                break
        j=i
        while(i<len(s)):
            if(j-i==0 and s[i]=="-"):
                sign=-1
                i+=1
            elif(j-i==0 and s[i]=="+"):
                sign=1
                i+=1
            elif(s[i]<"0" or s[i]>"9"):
                break
            else:
                res=res*10+int(s[i])
                i+=1
        res=res*sign
        if(res<-n):
            return(-n)
        elif(res>n-1):
            return(n-1)
        else:
            return res