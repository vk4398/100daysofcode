class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(len(s)<2 or numRows<2):
            return s
        l=[""]*numRows
        c=0
        i,j=0,1
        for x in range(len(s)):
            if(i==0):
                j=1
            elif(i==numRows-1):
                j=-1
            l[i]+=s[x]
            i+=j
            
        return ''.join(l)