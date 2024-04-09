from sys import stdin
input = stdin.readline


# 인덱스는 1부터 시작한다고 생각
def heap_up(heap):
    node = len(heap) - 1 # 마지막 노드 올리기
    while True:
        parent = node // 2

        if parent == 0 or heap[parent] >= heap[node]: break
        heap[parent], heap[node] = heap[node], heap[parent]
        
        node = parent

def heap_insert(heap, a):
    heap.append(a)
    heap_up(heap)

def heap_down(heap):
    node = 1 # 맨 위부터 차례로 내림
    while True:
        left, right = 2*node, 2*node+1
        l = len(heap)

        if l <= left: # 자식 노드, 없으면 
            break
        elif l<=right: # 왼쪽만 있는 경우
            if heap[left] > heap[node]:
                heap[node], heap[left] = heap[left], heap[node]
                node = left
            else: # 없으면 멈춤
                break
        else: # 양쪽 다 있는 경우
            if heap[left] > heap[right]: # 왼쪽 자식이 오른쪽 자식보다 더 크고
                if heap[left] > heap[node]: # 왼쪽 자식이 현재노드 보다 크면
                    heap[node], heap[left] = heap[left], heap[node]
                    node = left
                else:
                    break
            else: # 
                if heap[right] > heap[node]: # 오른쪽쪽 자식이 현재노드 보다 크면
                    heap[node], heap[right] = heap[right], heap[node]
                    node = right
                else:
                    break
    
def heap_delete(heap): # 맨 위에꺼 팝

    heap[1], heap[-1] = heap[-1], heap[1]
    result = heap.pop()
    heap_down(heap)
    return result
    
T = int(input())

for _ in range(T):
    k = int(input())
    max_heap = ['']
    min_heap = ['']
    num_dict = dict()

    for _ in range(k):
        order, num = map(str, input().split())
        num = int(num)
        if order == 'I':
            heap_insert(min_heap, -num)
            heap_insert(max_heap, num)
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        else:            
            if num == 1: # 최대값 제거
                while len(max_heap) > 1:                 
                    n = heap_delete(max_heap)
                    if num_dict[n] > 0: # 존재하는 값일 경우
                        num_dict[n] -= 1
                        break
            else:       
                while len(min_heap) > 1:       
                    n = -heap_delete(min_heap)
                    if num_dict[n] > 0:
                        num_dict[n] -= 1 
                        break
    num_lst = list(num_dict.items())


    num_lst.sort(key=lambda x:x[0], reverse=True)
    sum_, max_, min_ = 0, 0, 0
    flag = False
    for i in range(len(num_lst)):
        sum_ += num_lst[i][1]
        if flag == False and num_lst[i][1]>0:
            max_ = num_lst[i][0]
            flag = True
        if flag == True and num_lst[i][1] > 0:
            min_ = num_lst[i][0]

    if sum_ == 0: 
        print('EMPTY')
    else:
        print(max_, min_)
