# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = None

    def append(self,data):
        temp_node = ListNode(data)

        current = self.head

        if not current:
            self.head = temp_node
        else:
            while current:
                current = current.next
            current = temp_node

class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1: LinkedList[ListNode], l2: LinkedList[ListNode]) -> LinkedList[ListNode]:
        l1_stack = []
        l2_stack = []
        
        # stack에 node.data 넣기
        l1_current = l1.head
        while l1:
            l1_stack.append(l1_current)
            l1_current = l1_current.next

        l2_current = l2.head()
        while l2:
            l2_stack.append(l2_current)
            l2_current = l2_current.next

        # pop해서 숫자 만들기
        num1 = ""
        for i in range(len(l1_stack)):
            num1 = num1 + l1_stack.pop()

        num2 = ""
        for i in range(len(l2_stack)):
            num2 = num2 + l2_stack.pop()

        result = str(int(num1) + int(num2))

        result_linked_list = LinkedList()

        # print(result)
        for i in range(len(result),0,-1):
            result_linked_list.append(i)