from collections import defaultdict
from icecream import ic

texts = [
    ('今天天天天有天天最大的优惠！', 1),
    ('今天没有加班的话，赶快回家！', 0),
    ('不要等到明天！', 1),
]

def train(text,y):
    counts = defaultdict(int)
    yi_num = defaultdict(int)
    for line,yi in zip(text,y):
        yi_num[yi] += 1
        for c in set(line):
            counts[(c,yi)] += 1
    ic(yi_num)
    ic(counts)
    probs = defaultdict(lambda :1/len(set(''.join(text))))

    for c_y, t in counts.items():
        c,y = c_y
        probs[(c, y)] = counts[c_y] / yi_num[y]
    ic(probs)


train([x for x,y in texts],[y for x,y in texts])