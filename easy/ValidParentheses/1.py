class Solution:
    couple={
        ')':'(',
        ']':'[',
        '}':'{'
    }

    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        for x in s:
            if x in self.couple.values():
                stack.append(x)
                i=i+1
            else:
                i=i-1
                if i<0:return False
                elif stack[i]==self.couple[x]:
                    stack.pop()
                else:
                    return False
        if i==0:
            return True
        else:
            return False

if __name__=='__main__':
    print(Solution().isValid("{[]}"))