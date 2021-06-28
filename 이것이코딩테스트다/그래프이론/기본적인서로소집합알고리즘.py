# 전체 시간복잡도: O(VM)
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:  # parent[4] (1) != 4, parent[1] == 1
        return find_parent(parent, parent[x])  # find_parent(parent, 1)
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    print(parent)
    x = find_parent(parent, a)  # 2
    y = find_parent(parent, b)  # 4
    print(f'x={x}, y={y}')
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화
# print(parent)  # 예상 [0,0,0,0,0,0,0] 맞음

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
# print(parent)  # 예상 [0,1,2,3,4,5,6] 맞음

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
print()
