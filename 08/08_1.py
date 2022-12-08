data = [ line for line in open(0).read().splitlines()]

counter = {}

for i,row in enumerate(data[1:-1],1):
    for j,col in enumerate(row[1:-1],1):
        if max(data[i][:j])<col  or  max(data[i][j+1:]) < col:
            if not counter.get(f'{i}{j}'):
                counter[f'{i:02}{j:02}'] = 1

data = list(zip(*data))

for i,row in enumerate(data[1:-1],1):
    for j,col in enumerate(row[1:-1],1):
        if max(data[i][:j])<col  or  max(data[i][j+1:]) < col:
            if not counter.get(f'{j}{i}'):
                counter[f'{j:02}{i:02}'] = 1

sol = len(counter) + 2*len(data) + 2*(len(data[0])) - 4
print(sol)