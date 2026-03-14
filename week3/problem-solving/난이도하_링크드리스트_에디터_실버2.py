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
    def __init__(self, cursor):
        self.cursor = cursor
        self.head = None

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
        # TODO: 커서 전 노드 찾기
        # TODO: 커서에 해당하는 값 찾기
        else:
            current = self.head
            while current:
                current = current.next
            # 커서 왼쪽 값 구함
            # 새로운 노드의 next를 커서 왼쪽 값의 next로, 커서 왼쪽 값의 next를 새로운 노드로 변경해야함
        self.cursor += 1
    
    def move_left(self):
        if not self:
            cursor -= 1

    def move_right(self):
        if not cursor == len(self):
            cursor += 1

    def delete_left(self):
        current = self.head
        if self:
            if len(self) == 1:
                self.head = None
            else :
                for i in range(self.cursor):
                    current = current.next
                # 커서 왼쪽 값을 구한 상태
                # 커서 왼쪽의 왼쪽 값의 next를 커서가 가리키는 값으로 변경해야 함
                cursor -= 1

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
    str = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())

    linked_list = LinkedList(len(str))    # cursor 문장의 맨 끝에 위치

    for i in range(len(str)):
        linked_list.append(str[i])

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
    print(f"{result}")