# 그리디 알고리즘(탐욕법, Greedy Algorithm)은 각 단계에서 가장 최적인 선택을 하는 알고리즘입니다. 
# 현재 상황에서 가장 좋아 보이는 선택을 하며 지속적으로 그 선택을 업데이트하며 최종적인 해답에 도달합니다.
# 이 선택이 미래에 불러올 영향은 생각하지 않습니다.
# 그러므로 항상 최적의 해를 갖는 건 아니다.
# 이 알고리즘은 전체적인 최적해를 찾기 위해 각 단계에서 지역적으로 최적인 선택을 하는 것으로 설계되어 있습니다.

###################################################################################

# 1. 거스름돈 문제

def greedy_coin_change(money):
    coins = [500, 100, 50, 10]
    count = 0

    for coin in coins:
        count += money // coin  # 해당 동전으로 최대한 많이 거슬러줄 수 있는 개수를 더함
        money %= coin  # 남은 돈을 갱신

    return count

total_money = 1260
result = greedy_coin_change(total_money)
print(result)  # 출력: 6 (500원 동전 2개, 100원 동전 2개, 50원 동전 1개, 10원 동전 1개)
# 이 코드에서는 가장 큰 동전부터 최대한 많이 사용하여 거스름돈을 주는 방식으로 구현되어 있습니다. 
# 이는 그리디 알고리즘의 일종으로, 각 단계에서 지역적으로 최적의 선택을 하는 것이 전체적으로 최적의 해를 만들어 냅니다.

#####################################################################################

# 2. 회의실 배정 문제

#여러 개의 회의가 있을 때, 각 회의는 시작 시간과 종료 시간이 주어집니다.
# 한 회의실에서 최대한 많은 회의를 진행할 수 있는 경우를 찾는 문제입니다. 
# 여러 회의가 겹치지 않고 최대한 많은 회의를 배정하는 것이 목표입니다.

def greedy_meeting_schedule(meetings):
    # 종료 시간을 기준으로 정렬
    sorted_meetings = sorted(meetings, key=lambda x: x[1])
    
    selected_meetings = []
    end_time = 0

    for meeting in sorted_meetings:
        start, end = meeting
        if start >= end_time:  # 현재 회의가 이전 회의가 끝난 시간 이후에 시작하면 선택
          # (현재에서 좋은 쪽만 선택)
            selected_meetings.append(meeting)
            end_time = end  # 현재 회의의 종료 시간 갱신

    return selected_meetings

# 예시 회의 일정 (시작시간, 종료시간)
meetings = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 8),
    (5, 9),
    (6, 10),
    (8, 11),
    (8, 12),
    (2, 13)
]

result = greedy_meeting_schedule(meetings)
print(result)
