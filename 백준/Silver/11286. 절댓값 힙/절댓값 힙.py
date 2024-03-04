from sys import stdin

class abs_min_heap:
    def __init__(self):
        self.arr = [None] # 0은 버리는 칸
        self.return_value = 0

    def abs_min_heap_up(self, k): # 인덱스 1이 루트 노트
        parent = k // 2 
        while parent >= 1 and abs(self.arr[parent]) >= abs(self.arr[k]):
            abs_p = abs(self.arr[parent])
            abs_k = abs(self.arr[k])
            if abs_p == abs_k: # 같다면
                if self.arr[parent] >= self.arr[k]: # 실제값 비교해서 더 작으면 올린다.
                    self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent] 
            elif abs_p > abs_k: # 부모가 더 크면 스왑
                self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent] 
            k = parent # 다음 부모로 넘어감
            parent = parent // 2

            
    def abs_min_heap_down(self, k): # 자식 노드중 더 큰 값과 교환
        
        l = len(self.arr)

        while k < l:
            left_child = k * 2
            right_child = k * 2 + 1
        

            if left_child >= l: # 자식 아예 없는 경우
                break
            else:
                abs_left = abs(self.arr[left_child])
                abs_k = abs(self.arr[k])
                if right_child >= l: # 왼쪽 자식만 있으면 비교후 왼쪽으로 내림
                    if abs_left == abs_k: #절대값 같다면
                        if self.arr[left_child] < self.arr[k]: #더 작은 애로
                            self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
        
                    elif abs_left < abs_k:
                        self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]

                    else:
                        break
                    k = left_child

                else: #양쪽 다 있으면 크기 비교 후 이동
                    abs_right = abs(self.arr[right_child])
                    
                    if abs_left == abs_right: # 절대값이 같다면
                        if self.arr[left_child] <= self.arr[right_child]: # 왼쪽 값이 더 작으면
                            if abs_left < abs_k: # 이동하는 애가 더 크면 스왑
                                self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                            elif abs_left == abs_k: # 같다면 크기 비교 후 스왑
                                if self.arr[left_child] <= self.arr[k]:
                                    self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                            else: break
                            k = left_child

                        else: # 오른쪽이 절대값 더 작으면 오른쪽이랑 비교
                            if abs_right < abs_k: # 오른쪽자식이 더 작다면 바꿈
                                self.arr[right_child], self.arr[k] = self.arr[k], self.arr[right_child]
                            elif abs_right == abs_k: # 절대값 같으면 실제값 비교
                                if self.arr[right_child] <= self.arr[k]:
                                    self.arr[k], self.arr[right_child] = self.arr[right_child], self.arr[k]
                            else: break
                            k = right_child

                    elif abs_left < abs_right: # 왼쪽 자식 절대값이 더 작으면
                        if abs_left < abs_k: # 이동하는 애가 더 크면 스왑
                                self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                        elif abs_left == abs_k: # 절대값 같다면
                            if self.arr[left_child] <= self.arr[k]: # 비교후 이동
                                self.arr[k], self.arr[left_child] = self.arr[left_child], self.arr[k]
                        else: break
                        k = left_child
                        
                    elif abs_left > abs_right: # 오른쪽 자식 절대값이 더 작으면
                        if abs_right < abs_k: # 오른쪽자식이 더 작다면 바꿈
                            self.arr[right_child], self.arr[k] = self.arr[k], self.arr[right_child]

                        elif abs_right == abs_k: # 절대값 같으면 실제값 비교
                            if self.arr[right_child] <= self.arr[k]:
                                self.arr[k], self.arr[right_child] = self.arr[right_child], self.arr[k]
                        else: break
                        k = right_child

                        

    def insert(self, element):
        self.arr.append(element)
        self.abs_min_heap_up(len(self.arr)-1)
    
    def del_abs_min(self):
        if len(self.arr) == 1: return 0
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1] 
        # 맨 위 노드와 맨 밑 노드 스왑
        self.return_value = self.arr.pop()
        self.abs_min_heap_down(1)
        return self.return_value

input = stdin.readline

n = int(input())
heap = abs_min_heap()
answer = []
for _ in range(n):
    num = int(input())
    if num == 0:
        answer.append(heap.del_abs_min())

    else:
        heap.insert(num)

for a in answer:
    print(a)