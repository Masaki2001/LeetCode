# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #         cur = head
        #         values = []
        #         while cur:
        #             values.append(cur.val)
        #             cur = cur.next

        #         cur = head
        #         while cur:
        #             cur.val = values.pop()
        #             cur = cur.next

        #         return head

        prev = None
        cur = head
        while cur:
            nextCur = cur.next
            cur.next = prev
            prev = cur
            cur = nextCur
        head = prev

        return head