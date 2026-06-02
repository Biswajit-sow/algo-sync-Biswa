# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head,times):
            curr=head
            prev=None
            while curr and times > 0:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
                times -= 1
            return 
        if head==None:
            return head
        new_head=None
        next_left=None
        prev_left=None
        size=2
        while (True):
            left=head
            right=head
            count=1
            while count < size and right:
                right=right.next
                count += 1
            if right:
                next_left=right.next
                reverse(left,size)
                if prev_left:
                    prev_left.next=right
                if new_head is None:
                    new_head= right
                prev_left=left# for next iteration 
                head=next_left
            else:# now right null when only one node left 
                if prev_left:
                    prev_left.next=left
                    # if there is one element then and left = head then till the res is null becuase there is one node so no change in prev ornext left or no right for this 
                if new_head==None:
                    new_head=left
                break
        return new_head