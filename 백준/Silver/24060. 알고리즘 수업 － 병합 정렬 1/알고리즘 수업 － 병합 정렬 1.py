import sys

def merge_sort(arr): # 메모리 효율이 좋지 않음
    if len(arr) == 1: # 가장 잘게 잘랐을 때(원소 하나만)
        return arr
    mid = (len(arr) + 1) // 2 # 중간을 자름(앞이 크도록 병합)
    left_arr = merge_sort(arr[:mid]) # 배열 계속 잘라줌
    right_arr = merge_sort(arr[mid:]) # 배열 잘라줌

    merged_arr = [] # 병합한 배열
    left , right = 0, 0 # 
    while left < len(left_arr) and right < len(right_arr): # left와 right가 길이와 같아질 때까지
        if left_arr[left] < right_arr[right]: # 오른쪽이 더 크면 왼쪽 먼저 넣음
            merged_arr.append(left_arr[left])
            ans.append(left_arr[left])
            left += 1
        else: # 왼쪽 애가 더 크면 왼쪽애 먼저 넣음
            merged_arr.append(right_arr[right])
            ans.append(right_arr[right])
            right += 1
    while left < len(left_arr): # left나 right만 먼저 만족되면 반복문 나가게 되므로 보완해줌
            merged_arr.append(left_arr[left])
            ans.append(left_arr[left])
            left += 1      
    while right < len(right_arr):
            merged_arr.append(right_arr[right])
            ans.append(right_arr[right])
            right += 1      
    return merged_arr


n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:   
    print(-1)