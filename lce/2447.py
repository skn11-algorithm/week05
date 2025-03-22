def draw_star(x, y, size):
    if size == 1:
        board[x][y] = '*'
        return

    next_size = size // 3
    for i in range(3):
        for j in range(3):
            # 가운데 블록은 비워두기
            if i == 1 and j == 1:
                continue
            draw_star(x + i * next_size, y + j * next_size, next_size)

n = int(input())
board = [[' ' for _ in range(n)] for _ in range(n)] 

draw_star(0, 0, n)

for row in board:
    print(''.join(row))
