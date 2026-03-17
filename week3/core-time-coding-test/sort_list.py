# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        if not head:
            return None

        while head.next:
            # 나누고, 계산하고, 합치고
            if current.val > current.next.val:
                temp = current
                current = current.next
                current.next = temp

            else: current = current.next