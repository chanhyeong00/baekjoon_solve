import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
num = len(A)

for i in range(len(A)):
    A[i] -= B # 총감독관 투입
     # 부감독관 투입
    if A[i] > 0: # 남은 학생이 있는 경우 부감독관 투입 수 계산
        k = A[i] // C
        rem_k = A[i] % C
        if rem_k > 0:
            num += (k+1)
        else:
            num += k

print(num)