import sys

# 1과 0만으로 구성됐는지 확인하는 재귀함수
def divide(input_list,x,y,size):
    first = int(input_list[x][y])

    # 순회
    for i in range(0,size):
        for j in range(0,size):
            # first는 비교 대상에서 제외

            if i == 0 and j == 0:
                continue
            
            if int(input_list[x+i][y+j]) != first:
                n = size // 2
                n1 = divide(input_list,x,y,n)
                n2 = divide(input_list,x,y+n,n)
                n3 = divide(input_list,x+n,y,n)
                n4 = divide(input_list,x+n,y+n,n)

                num_w = n1[0] + n2[0] + n3[0] + n4[0]
                num_b = n1[1] + n2[1] + n3[1] + n4[1]

                return(num_w, num_b)

    # white
    if first == 0:
        return (1, 0)
    # blue
    else:
        return (0, 1)

# 입력 받은 데이터를 2차원 배열에 매핑
n = int(sys.stdin.readline().strip())

input_list = [[0 for i in range(n)] for j in range(n)]

# print(input_list)

for x in range(n):
    input_list[x] = (sys.stdin.readline().strip()).split(" ")

# print(input_list)

# 4등분 후 재귀함수 호출
result = divide(input_list,0,0,n)

print(result[0])
print(result[1])