class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = ""
        length = len(strs)
        if length < 2 and length > 0:
            return strs[0]

        elif length == 0:
            return ""
        else:
            i = 0
            while (i < len(strs[0]) and i < len(strs[1])):
                if strs[0][i] == strs[1][i]:
                    prefix = prefix + strs[0][i]
                    i = i + 1
                else:
                    break
            for i in range(2, len(strs)):
                j = 0
                if len(prefix)<len(strs[i]):
                    j=len(prefix)
                else:
                    j=len(strs[i])
                    prefix=prefix[:j]
                k=0
                while(k<j):
                    if prefix[k] == strs[i][k]:
                        k = k + 1
                    else:
                        if k < len(prefix):
                            prefix = prefix[:k]
                            break
                if k==0:
                    return ""
            return prefix

if __name__=='__main__':
    print(Solution().longestCommonPrefix(["ac","ac","a","a"]))