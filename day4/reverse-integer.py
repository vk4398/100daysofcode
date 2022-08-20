class Solution:
    def reverse(self, x: int) -> int:
        s=1
        if(x<0):
            s=-1
        x*=s
        res=0
        n=2**31
        while(x>0):
            res=res*10+x%10
            x=int(x/10)
        if(res*s<-n or res*s>n-1):
            return 0
        else:
           return res*s