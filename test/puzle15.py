def get_digit(pos):
    return (pos[0] * 4 + pos[1]) * 4


def get_val(pl, pos):
    pl >>= get_digit(pos)
    return pl & 0b1111


def puzzle_input():
    pl = 0
    emp = None
    for x in range(4):
        vals = list(map(int, input().split()))
        for y in range(4):
            if vals[y] == 0:
                emp = (x, y)
            else:
                pl += vals[y] << get_digit((x, y))
    return pl, emp


def puzzle_print(pl):
    for x in range(4):
        print(*map(lambda e:f"{e:>2}", [get_val(pl, (x, y)) for y in range(4)]))

def slide(pl, val, pos, emp):
    pl -= val << get_digit(pos)
    pl += val << get_digit(emp)
    return pl


def calc_distance(val, pos):
    x, y = (val - 1) // 4, (val - 1) % 4
    return abs(x - pos[0]) + abs(y - pos[1])


def init_estimate(pl):
    res = 0
    for x in range(4):
        for y in range(4):
            val = get_val(pl, (x, y))
            if val == 0:
                continue
            res += calc_distance(val, (x, y))
    return res


def estimate(est, val, pos, emp):
    return est + calc_distance(val, emp) - calc_distance(val, pos)


def dfs(max_depth, depth, pl, emp, est, pre_dir, res):
    DX = [1, 0, -1, 0]
    DY = [0, 1, 0, -1]
    if res:
        return res
    if est == 0:
        res.append(pl)
        return res
    if depth >= max_depth:
        return res
    for dir in range(4):
        reverse_dir = (dir + 2) % 4
        if reverse_dir == pre_dir:
            continue
        nx = emp[0] + DX[dir]
        ny = emp[1] + DY[dir]
        pos = (nx, ny)
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        val = get_val(pl, pos)
        next_pl = slide(pl, val, pos, emp)
        next_est = estimate(est, val, pos, emp)
        if depth + next_est <= max_depth:
            res = dfs(max_depth, depth + 1, next_pl, pos, next_est, dir, res)
            if res:
                res.append(pl)
                return res


def solv(pl, emp):
    est = init_estimate(pl)
    for max_depth in range(80 + 1):
        res = []
        res = dfs(max_depth, 0, pl, emp, est, -1, res)
        if res:
            res.reverse()
            return res
    return []


if __name__ == "__main__":
    print("15puzzle input:")
    pl, emp = puzzle_input()
    res = solv(pl, emp)
    for i in range(len(res)):
        print("-----")
        print(f"{i} th move: ")
        puzzle_print(res[i])