# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# 맥 EOF 처리 단축키 : Ctrl + D

"""
postorder(시작, 끝):
    루트 = preorder[시작]
    경계 찾기
    postorder(왼쪽 구간)
    postorder(오른쪽 구간)
    print(루트)
"""

import sys

preorder_result = []

def postorder(list, start, end):
    root = preorder_result[start]

for line in sys.stdin:
    preorder_result.append(int(line.strip()))

postorder(preorder_result, 0, len(preorder_result)-1)

