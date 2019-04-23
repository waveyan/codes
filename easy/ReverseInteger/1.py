class Solution:
    '''负数取余，-11//-10=1，-11%-10=-1
    %负数，余数为负
    /负数，商为正
    32bit 最大值:2^31-1
    最小值：-2^31=
    '''
    def reverse(self, x: int) -> int:
        result=0
        while(x!=0):
            if x>0:
                result=result*10+x%10
                x=x//10
            else:
                result=result*10+x%(-10)
                x=(x//-10)*-1
        if result>2147483647 or result<-2147483648:
            return 0
        return result

if __name__=='__main__':
    print(Solution().reverse(-120))

