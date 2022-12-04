import sys

p1 = 0
p2 = 0

for i in sys.stdin:
    a, b = i.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))


    #part1
    if a1 <= b1 and a2 >= b2:
        p1+=1
    elif b1 <= a1 and  b2 >= a2:
        p1 += 1

    #part2
    if a1 <= b1 and a2 >= b1:
        p2+=1
    elif b1 <= a1 and  b2 >= a1:
        p2 += 1

print(p1)

print(p2)