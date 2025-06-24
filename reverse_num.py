class Solution(object):
    def isPalindrome(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False

        reversed=0
        original=x

        while x>0:
            digit=x%10
            reversed=reversed*10 + digit 
            x//=10

        return original==reversed

        