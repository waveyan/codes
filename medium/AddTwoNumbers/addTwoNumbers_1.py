#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=self.initNum(l1)
        n2=self.initNum(l2)
        s=n1+n2
        t = s % 10
        s = s // 10
        p=ListNode(t)
        r=p
        while( not s == 0):
            t=s%10
            s=s//10
            #同文件系统，对象引用计数为0时被回收
            l=ListNode(t)
            p.next=l
            p=l
        return r


    def initNum(self,l:ListNode):
        i=0
        t=[]
        result=0
        while(not l == None):
            t.append(l.val)
            l=l.next
            i=i+1
        for j in range(i-1,-1,-1):
            result=t[j]+result*10
        return result


if __name__=='__main__':
    l1=ListNode(2)
    l2=ListNode(4)
    l3=ListNode(3)
    l1.next=l2
    l2.next=l3
    l11=ListNode(5)
    l21=ListNode(6)
    l31=ListNode(4)
    l11.next=l21
    l21.next=l31
    s=Solution()
    print(s.initNum(s.addTwoNumbers(l1,l11)))
