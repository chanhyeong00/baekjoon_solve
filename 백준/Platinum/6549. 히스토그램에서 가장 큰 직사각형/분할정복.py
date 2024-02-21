from sys import stdin


input = stdin.readline

def hist(start, end):
    if start == end:
        return h[start]
    
    mid = (start + end) // 2 # 가운데 분할
    left = mid
    right = mid + 1 # 오른쪽

    min_h = min(h[mid], h[right]) # 경계선 기준 두개중 낮은 애로 높이 기준(얘로 확장)
    width = 2 # 너비
    area = min_h * width # 경계선에 걸친 직사각형의 넓이

    # 3가지 경우 : 경계선 왼쪽, 경계선 포함, 경계선 오른쪽

    # mid와 m_right 기준으로 한칸씩 좌. 우로 넓혀간다

    # 1. 경계선 포함하고, 낮은 높이를 찾아서 최대 넓이(좌우 확장하며)
    while (left > start) or (right < end):
        if right < end and (left == start or h[left - 1] < h[right + 1]): 
            # 끝지점까지 오지 않고, 왼쪽 끝 지점에 도달했으면 오른쪽 확장
            # 끝지점까지 오지 않고, 오른쪽 높이가 왼쪽보다 더 높으면 오른쪽 확장(낮으면 어차피 끊김)
            right += 1
            min_h = min(min_h, h[right])
        else: # 왼쪽이 더 높으면 왼쪽으로 확장(기준이 경계선 기준 2개중 낮은애)
            left -= 1
            min_h = min(min_h, h[left])
        width = right - left + 1
        area = max(area, min_h * width)
    
    left_area = hist(start, mid) # 2. 왼쪽
    right_area = hist(mid+1, end) # 3. 오른쪽

    return max(area, left_area, right_area)

while True:
    n, *h = list(map(int, input().split()))
    if n == 0:
        break
    mem = {}
    h_set = set(h)

    print(hist(0, n-1))
    
    # https://bingorithm.tistory.com/14
