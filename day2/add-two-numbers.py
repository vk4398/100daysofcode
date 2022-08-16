class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        temp = head
        sum=0
        while(l1 or l2 or sum):
            if(l1):
                sum+=l1.val
                l1=l1.next
            if(l2):
                sum+=l2.val
                l2=l2.next
            node=ListNode()
            node.val=sum%10
            temp.next=node
            temp=node
            
            sum=int(sum/10)
        return head.next
        return res.next
