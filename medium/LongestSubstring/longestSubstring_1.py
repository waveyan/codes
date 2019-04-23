class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        r=0
        t={}
        i=0
        while(i<length):
            idx=t.get(s[i],None)
            if not idx:
                t[s[i]]=i
            else:
                i=idx
                t.clear()
            i=i+1
            if r<len(t.keys()):
                r=len(t.keys())
        return r

if __name__=='__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))


