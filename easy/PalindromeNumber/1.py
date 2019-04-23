class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        start=0
        end=len(str_x)-1
        while start!=end and start<end:
            if str_x[start]==str_x[end]:
                start=start+1
                end=end-1
            else:
                return False
        return True

if __name__=='__main__':
    print(Solution().isPalindrome(11))

