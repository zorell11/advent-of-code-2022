data = [line for line in open(0).read().splitlines()]

counter = {}

for i,row in enumerate(data[1:-1],1):
    for j,col in enumerate(row[1:-1],1):
        if not counter.get(f'{i:02}{j:02}'):
            counter[f'{i:02}{j:02}'] = 1
        tree = 0
        
        for k in range(j-1,-1,-1):
            tree +=1
            if data[i][j] <= data[i][k]:
                counter[f'{i:02}{j:02}'] *= tree
                tree = 0
                break
        if tree:
            counter[f'{i:02}{j:02}'] *= tree

        tree = 0
        for k in range(j+1,len(row),1):
            tree +=1
            if data[i][j] <= data[i][k]:
                counter[f'{i:02}{j:02}'] *= tree
                tree = 0
                break
        if tree:
            counter[f'{i:02}{j:02}'] *= tree
        
data = list(zip(*data))

for i,row in enumerate(data[1:-1],1):
    for j,col in enumerate(row[1:-1],1):
        if not counter.get(f'{j:02}{i:02}'):
            counter[f'{j:02}{i:02}'] = 1
        tree = 0  
        for k in range(j-1,-1,-1):
            tree +=1
            if data[i][j] <= data[i][k]:
                counter[f'{j:02}{i:02}'] *= tree
                tree = 0
                break
        if tree:
            counter[f'{j:02}{i:02}'] *= tree

        tree = 0
        for k in range(j+1,len(row),1):
            tree +=1
            if data[i][j] <= data[i][k]:
                counter[f'{j:02}{i:02}'] *= tree
                tree = 0
                break
        if tree:
            counter[f'{j:02}{i:02}'] *= tree

print(max(sorted(counter.values())))