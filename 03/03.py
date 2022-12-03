def count_value(common):
    prio = 0
    for i in common:
        if i.islower():
            prio += ord(i) - ord('a') + 1 
            continue
        prio +=  ord(i) - ord('A') + 1 + 26
    return prio



with open('input', 'r') as f:
    data = f.read().splitlines()

# task1
common1 = []
for rucksack in data:
    half = len(rucksack)//2
    common1 += (list(set(rucksack[:half]) & set(rucksack[half:])))
print(count_value(common1))


#task2
common2 = []
for i in range(0,len(data),3):
    common2 += list(set(data[i]) & set(data[i+1]) & set(data[i+2]))
print(count_value(common2))
