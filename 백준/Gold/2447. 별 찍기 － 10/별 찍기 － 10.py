import sys

def draw_stars(n):
    if n == 3:
        return ["***","* *", "***"]
    stars = draw_stars(n//3)
    arr = []

    for star in stars: # 위
        arr.append(star * 3)
    for star in stars: # 중간(공백 넣는 부분)
        arr.append(star + " " * (n//3) + star)
    for star in stars: # 아래
        arr.append(star * 3)
    return arr
n = int(sys.stdin.readline().strip())
print("\n".join(draw_stars(n)))