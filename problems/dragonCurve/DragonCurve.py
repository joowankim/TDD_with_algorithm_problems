d = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}


def c_rotate(x, y):
    return -y, x


def rotate(x, y, ex, ey):
    cx, cy = x - ex, y - ey
    rx, ry = c_rotate(cx, cy)
    return rx + ex, ry + ey


class DragonCurve:
    def __init__(self, sx, sy, direction, gen):
        self.start = (sx, sy)
        self.direction = d[direction]
        self.gen = gen


class Board:
    def __init__(self):
        self.board = [[0] * 101 for _ in range(101)]

    def draw_curve(self, curve):
        sx, sy = curve.start
        dx, dy = curve.direction
        ex, ey = sx + dx, sy + dy
        self.board[sy][sx] = 1
        self.board[ey][ex] = 1

        points = [(sx, sy), (ex, ey)]
        for _ in range(curve.gen):
            next_points = []
            for px, py in points:
                nx, ny = rotate(px, py, ex, ey)
                self.board[ny][nx] = 1
                next_points.append((nx, ny))
            ex, ey = rotate(sx, sy, ex, ey)
            points += next_points

    def __is_sqr(self, x, y):
        if self.board[y][x] == 1 and \
                self.board[y + 1][x] == 1 and \
                self.board[y][x + 1] == 1 and \
                self.board[y + 1][x + 1] == 1:
            return True
        return False

    def get_sqr_count(self):
        cnt = 0
        for i in range(100):
            for j in range(100):
                if self.__is_sqr(i, j):
                    cnt += 1
        return cnt


if __name__ == "__main__":
    N = int(input())
    curves = [DragonCurve(*(map(int, input().split()))) for _ in range(N)]
    board = Board()
    for curve in curves:
        board.draw_curve(curve)
    print(board.get_sqr_count())
