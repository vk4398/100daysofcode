class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        rev=0
        n=x
        while(n>9):
            rev=rev*10+n%10
            n=int(n/10)
        rev=rev*10+n
        if rev==x:
            return True
        return False