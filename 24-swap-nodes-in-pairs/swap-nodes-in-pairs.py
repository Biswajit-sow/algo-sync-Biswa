# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head, times):
            curr = head
            prev = None

            while curr and times > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                times -= 1

            return prev

        if head is None:
            return head

        res = None
        prev_left = None
        size = 2

        while True:

            left = head
            right = head

            count = 1
            while count < size and right:
                right = right.next
                count += 1

            if right:
                next_left = right.next

                reverse(left, size)

                if prev_left:
                    prev_left.next = right

                if res is None:
                    res = right

                prev_left = left
                head = next_left

            else:
                if prev_left:
                    prev_left.next = left

                if res is None:
                    res = left

                break

        return res