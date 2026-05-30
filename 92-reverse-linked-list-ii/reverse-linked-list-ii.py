# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None

        if left == right:
            return head

        t = head
        before = None
        pos = 1

        while t != None:
            if pos < left:
                before = t
                t = t.next
                pos += 1
            else:
                break

        # pos = left
        # now reverse
        curr = t
        prev = None
        times = right - left + 1

        while times > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            times -= 1

        # now attach last two connections
        # end node to left position node
        t.next = curr

        # first node to right position node
        if before != None:
            before.next = prev
            return head
        else:
            return prev