# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        # 1) base case
        if not head:
            return None
        
        if not head.next:
            return head

        # 2) slow/fast로 중간 찾기
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 3) 반으로 끊기
        mid = slow.next
        slow.next = None

        # 4) 왼쪽 정렬
        left = self.sortList(head)
        # 5) 오른쪽 정렬
        right = self.sortList(mid)

        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        if left:
            cur.next = left
        else:
            cur.next = right

        return dummy.next