import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
paper = []
idx = 1
for _ in range(n):
    row = list(map(int, data[idx:idx+n]))
    paper.append(row)
    idx += n

white = 0
blue = 0

def divide(x, y, size):
    global white, blue
    first = paper[x][y]
    all_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if first == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        divide(x, y, half)             # 왼쪽 위
        divide(x, y + half, half)      # 오른쪽 위
        divide(x + half, y, half)      # 왼쪽 아래
        divide(x + half, y + half, half)  # 오른쪽 아래

# 시작 호출
divide(0, 0, n)

print(white)
print(blue)
