from icecream import ic


def successor(x, y, X, Y):
    return {
        (0, y): '倒空x',
        (x, 0): '倒空y',
        (X, x + y - X) if x + y > X else (x + y, 0): '将y倒入x',
        (x + y - Y, Y) if x + y > Y else (0, x + y): '将x倒入y',
        (X, y): '装满X',
        (x, Y): '装满Y'
    }


def search_solution(capacity1, capacity2, goal, start=(0, 0)):
    # 利用一个二维列表记录路径，每一个路径为一个列表，列表中的元素由（action,state）组成
    paths = [[('init', start)]]
    explored = set()

    while paths:
        path = paths.pop(0)
        frontier = path[-1]

        state = frontier[-1]
        x, y = state

        for state, action in successor(x, y, capacity1, capacity2).items():
            if state in explored: continue
            new_path = path + [(action, state)]
            ic(new_path)

            if goal in state:
                return new_path
            else:
                paths.append(new_path)
                ic(paths)
            explored.add(state)
    return None


if __name__ == '__main__':
    ic(successor(0, 0, 40, 90))
    path = search_solution(90, 40, 60)
    for p in path:
        print('->')
        print(p)