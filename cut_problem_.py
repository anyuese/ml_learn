from collections import defaultdict
from functools import lru_cache

from icecream import ic

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]

length_prices = defaultdict(int)
for i, p in enumerate(prices): length_prices[i + 1] = p
ic(dict(length_prices))


# 计算如何切木材的收益最大
def revnue(n, cache={}):
    if n in cache: return cache[n]
    candidates = [length_prices[n]]
    for i in range(1, n):
        candidate = revnue(i, cache) + revnue(n - i, cache)
        candidates.append(candidate)
    max_profit = max(candidates)
    cache[n] = max_profit
    return max_profit

ic(revnue(118))


# 计算切木材收益最大,并能提取怎么切
def revnue_solution(n, solutions={}, cache={}):
    if n in cache: return cache[n], solutions[n]
    candidates = [(length_prices[n], (n, 0))]
    for i in range(1, n):
        candidate = (revnue_solution(i, solutions, cache)[0] + revnue_solution(n - i, solutions, cache)[0], (i, n - i))
        candidates.append(candidate)
    max_profit, solution = max(candidates, key=lambda x: x[0])
    cache[n] = max_profit
    solutions[n] = solution
    return max_profit, solutions

ic(revnue_solution(118))
ic(revnue_solution(18))
# ic(revnue_solution(118))

# 解析路径
def parse_solution(path, n):
    i, j = path[n]
    if j == 0:
        return path[n]
    else:
        return parse_solution(path, i) + parse_solution(path, j)


# ic(parse_solution(revnue_solution(118)[1], 118))
# ic(revnue_solution(8))
SOLUTIONS = {}


@lru_cache(maxsize=2 ** 10)
def revnue_solution_cache(n):
    candidates = [(length_prices[n], (n, 0))]
    for i in range(1, n):
        candidate = (revnue_solution_cache(i) + revnue_solution_cache(n - i), (i, n - i))
        candidates.append(candidate)

    global SOLUTIONS
    max_profit, solution = max(candidates, key=lambda x: x[0])
    SOLUTIONS[n] = solution
    return max_profit


# ic(revnue_solution_cache(200))
# ic(SOLUTIONS)
# ic(parse_solution(SOLUTIONS,200))
