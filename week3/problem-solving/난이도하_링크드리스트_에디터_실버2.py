# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys

class Node:
    """연결 리스트의 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """단순 연결 리스트"""
    def __init__(self, cursor, length):
        self.cursor = cursor
        self.head = None
        self.length = length

    def append(self, data):
        """리스트 끝에 노드 추가"""
        new_node = Node(data)
        
        # TODO: 리스트가 비어있으면 head를 new_node로 설정
        if not self.head:
            self.head = new_node
        
        # TODO: 마지막 노드 찾기
        # TODO: 마지막 노드의 next를 new_node로 설정
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
    
    def append_left(self, data):
        """커서 왼쪽에 노드 추가"""
        new_node = Node(data)
        
        # TODO: 리스트가 비어있으면 head를 new_node로 설정
        if not self.head:
            self.head = new_node

        elif self.cursor == 0:
            new_node.next = self.head
            self.head = new_node

        # TODO: 커서 전 노드 찾기
        # TODO: 커서에 해당하는 값 찾기
        else :
            current = self.head

            for i in range(self.cursor - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.cursor += 1
        self.length += 1
    
    def move_left(self):    # self는 LinkedList 객체 자체
        if self.cursor > 0:
            self.cursor -= 1

    def move_right(self):
        if self.cursor < self.length:
            self.cursor += 1

    def delete_left(self):
        if self.cursor == 0:
            return
        
        if self.cursor == 1:
            self.head = self.head.next
        else :
            current = self.head

            for i in range(self.cursor - 2):
                current = current.next
            
            current.next = current.next.next
        
        self.cursor -= 1
        self.length -= 1

    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []
        
        # TODO: head부터 시작
        
        # TODO: 끝까지 순회하며 값 수집
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values
    
if __name__ == "__main__":
    input = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())

    linked_list = LinkedList(len(input), len(input))    # cursor 문장의 맨 끝에 위치

    for i in range(len(input)):
        linked_list.append(input[i])

    # print("입력 직후 linked_list:")
    # result = linked_list.print_list()
    # for i in range(len(result)):
    #     print(result[i])

    for j in range(m):
        item = sys.stdin.readline().strip()
        if item[0] == "L":
            linked_list.move_left()
        elif item[0] == "D":
            linked_list.move_right()
        elif item[0] == "B":
            linked_list.delete_left()
        elif item[0] == "P":
            linked_list.append_left(item.split(" ")[1])

    result = linked_list.print_list()
    print("".join(result))