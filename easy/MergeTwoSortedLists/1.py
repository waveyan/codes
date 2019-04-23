class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''从小到大合并'''
        if l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val<l2.val:
            node=ListNode(l1.val)
            l1=l1.next
        else:
            node=ListNode(l2.val)
            l2=l2.next
        newList=node
        while l1!=None and l2!=None:
            if l2.val<l1.val:
                node.next=ListNode(l2.val)
                l2=l2.next
                node=node.next
            else:
                node.next=ListNode(l1.val)
                l1=l1.next
                node = node.next
        if l1!=None:
            node.next=l1
        elif l2!=None:
            node.next=l2
        return newList


if __name__=="__main__":
    l1=ListNode(1)
    temp1=ListNode(1)
    l1.next=temp1
    temp2=ListNode(4)
    temp1.next=temp2
    l2 = ListNode(1)
    temp1 = ListNode(3)
    l2.next = temp1
    temp2 = ListNode(4)
    temp1.next = temp2
    Solution().mergeTwoLists(l1,l2)
