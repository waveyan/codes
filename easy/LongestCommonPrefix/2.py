from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs)>1:
            return reduce(self.getPrefix,strs)
        elif len(strs)==1:
            return strs[0]
        else:
            return ""

    def getPrefix(self,x,y):
        to =0
        prefix=''
        if len(x)<len(y):
            to=len(x)
        else:
            to=len(y)
        if to==0:
            return ''
        for i in range(to):
            if x[i]==y[i]:
                prefix=prefix+x[i]
            else:
                break
        return prefix
if __name__=="__main__":
    print(Solution().longestCommonPrefix(["aca","cba"]))