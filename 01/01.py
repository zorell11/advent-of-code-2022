with open('input', 'r') as f:
    cals = f.read().splitlines()

total_cals = []
elf = 0
for cal in cals:    
    if cal:
        elf += int(cal)
    else:
        total_cals.append(elf)
        elf = 0
    
#part1
print(max(total_cals))

#part2
total_cals.sort(reverse=True)
print(sum(total_cals[:3]))

