import functools

with open('input') as f:
    data = f.read().split('\n\n')


def check(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l-r
    elif isinstance(l, int):
        return check([l], r)
    elif isinstance(r, int):
        return check(l, [r])

    for l1, r1 in zip(l,r):
        ch = check(l1, r1)
        if ch:
            return ch
    return len(l) - len(r)

all_item = []
for counter, line in enumerate(data, 1):
    left, right = line.split('\n')
    left1 = eval(left)
    right1 = eval(right)  
    all_item += [left1, right1]
 
all_item.append([[2]])
all_item.append([[6]])

z = sorted(all_item, key=functools.cmp_to_key(lambda x,y: check(x,y)))
print((z.index([[2]])+1) * (z.index([[6]])+1))