with open('input', 'r') as f:
    data = f.read().split('\n\n')
        
z = [ [j.strip() for j in i.split('\n')] for i in data]

monkeys = {}

for i in z:
    monkey = int(i[0].split()[1].strip(':'))
    items = [ int(j) for j in i[1].strip('Starting items: ').split(', ')]
    operation = eval('lambda old: ' + i[2].split('=')[1])
    div = int(i[3].strip('Test: divisible by '))
    fi = int(i[4].strip('If true: throw to monkey '))
    esle = int(i[5].strip('If false: throw to monkey '))
    activity = 0
    monkeys[monkey] = {'items': items, 'operation': operation, 'div': div, 'fi': fi, 'esle': esle, 'activity': activity}

for iteration in range(20):
    for monkey in monkeys.values():
        monkey['activity'] += len( monkey['items'])
        for old in monkey['items']:
            num = monkey['operation'](old)//3
            if num%monkey['div'] == 0:
                monkeys[monkey['fi']]['items'].append(num)
            else:
                monkeys[monkey['esle']]['items'].append(num)
            
        monkey['items'] = []
        
inspected = []
for i in monkeys:
    inspected.append(monkeys[i]['activity'])

inspected = sorted(inspected)
print(inspected[-1]*inspected[-2])