# 이미 진행이 되었던 연산이 반복되는 결점을 보안하기 위해 동적 계획법(Dynamic Programing, DP)가 고안되었다.
# 여러 개의 소문제로 분할하여 각 소문제의 해결안을 바탕으로 주어진 문제를 해결, 
# 이때 각 소문제는 다시 여러개의 소문제로 분할 가능하다.

# - 처음 진행되는 연산은 기록
# - 이미 진행됬던 연산이라면 다시 연산이라면 기록되어 있는 값을 호출
# - 시간 & 자원절약 가능

# ex ) 피보나치 수열
# 1. 재귀
def fibo(x):
	if x==1 or x==2:
    	return 1
    return fibo(x-1) + fibo(x-2)
# 2. 탑다운(top-down)
# 큰 문제 해결하기 위해 작은 문제 호출
# 한번 게산된 결과는 기록
memo = [0]*100

def fibo(x):
  # fibo(1)=fibo(2)=0
  if x==1 or x==2:
    return 1
  # 이미 계산한 적 있다면 그값 반환
  if memo[x] != 0:
    return memo[x]
  # 아직 계산하지 않은 문제라면(memo[x] == 0) 점화식에 따라서 피보나치 결과 반환
  memo[x] = fibo(x-1)+fibo(x-2)
  return memo[x]
  
# 3. bottom-up (작은 문제부터 차례로 올라감, 반복문으로 구현 가능)
memo2 = [0] * 100
memo2[1] = 1
memo2[2] = 1
n = 99 # 99번쨰 피보나치 수열

for i in range(3, n+1):
  memo2[i] = memo2[i-1] + memo2[i-2]
