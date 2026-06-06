# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        n=1
        last=head
        while(last.next!=None):
            n+=1
            last=last.next
        k=k%n
        if k==0:
            return head

        t=head
        count=1
        while t !=None:
            if count==(n-k):
                break
            count+=1
            t=t.next
            #now we got the n-k node and now do the 3 connection change
        last.next=head
        new_head=t.next
        t.next=None
        return new_head