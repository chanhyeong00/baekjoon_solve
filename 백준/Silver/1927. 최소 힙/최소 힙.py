from sys import stdin

class min_heap:
    def __init__(self):
        self.arr = [''] # 0은 버리는 칸
        self.return_value = 0

    def min_heap_up(self, k): # 인덱스 1이 루트 노트
        # 부모 * 2 = 왼쪽 자식, 부모 * 2 + 1 = 오른쪽 자식
        parent = k // 2  # 부모 = 왼쪽 or 오른쪽 자식 // 2
        while parent >= 1 and self.arr[parent] > self.arr[k]:
            self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent] 
            k = parent # 다음 부모로 넘어감
            parent = parent // 2

    def min_heap_down(self, k): # 자식 노드중 더 큰 값과 교환
        
        l = len(self.arr)

        while k < l:
            left_child = k * 2
            right_child = k * 2 + 1

            if left_child >= l: # 자식 아예 없는 경우
                break
            else:
                if right_child >= l: # 왼쪽 자식만 있으면 비교후 왼쪽으로 내림
                    if k < l and self.arr[left_child] < self.arr[k]:
                            self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                            k = left_child
                    else:
                        break
                else: #양쪽 다 있으면 크기 비교 후 이동
                    if self.arr[left_child] < self.arr[right_child]: # 왼쪽 자식이 작으면
                        if self.arr[left_child] < self.arr[k]: # 이동하는 애가 더 크면 스왑
                            self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                            k = left_child
                        else:
                            break
                    else: # 오른쪽 자식이 더 작고
                        # 오른쪽 자식이 부모노드보다 작으면
                        if self.arr[right_child] < self.arr[k]:
                            self.arr[right_child], self.arr[k] = self.arr[k], self.arr[right_child]
                            k = right_child
                            # 밑으로 내린다
                        else:
                            break

    def insert(self, element):
        self.arr.append(element)
        self.min_heap_up(len(self.arr)-1)
    
    def del_min(self):
        if len(self.arr) == 1: return 0
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1] 
        # 맨 위 노드와 맨 밑 노드 스왑
        self.return_value = self.arr.pop()
        self.min_heap_down(1)
        return self.return_value

input = stdin.readline

n = int(input())
heap = min_heap()
answer = []
for _ in range(n):
    num = int(input())
    if num == 0:
        answer.append(heap.del_min())
    else:
        heap.insert(num)

for a in answer:
    print(a)