# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_num = ""
        for i in range(len(l1_list)-1,-1,-1):
            l1_num = l1_num + str(l1_list[i])

        l2_num = ""
        for j in range(len(l2_list)-1,-1,-1):
            l2_num = l2_num + str(l2_list[j])

        #print(f"{l1_num} + {l2_num}")
        result = int(l1_num) + int(l2_num)

        result_str = str(result)

        head = None
        current = None

        for i in result_str[::-1]:
            node = ListNode(int(i))

            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node
        return head