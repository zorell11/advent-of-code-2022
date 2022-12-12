with open('input', 'r') as f:
    data = list(map(list, f.read().split()))


for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            S = (i,j)
            data[i][j] = 'a'
        if data[i][j] == 'E':
            E = (i,j)
            data[i][j] = 'z'

checked = {(S[0], S[1])}

queue = [(0, S[0], S[1])]

val = []
while queue:
    value, x, y = queue.pop(0)
    
    for x1,y1 in (x-1,y), (x, y+1), (x+1, y), (x, y-1):
        if x1<0 or y1<0 or x1>=len(data) or y1>= len(data[0]):
            continue

        if (x1,y1) in checked:
            continue

        if ord(data[x1][y1]) - ord(data[x][y]) > 1:
            continue
        
        if (x1,y1) == (E[0], E[1]):
            print(value+1)
            exit()

        checked.add((x1,y1))
        queue.append((value+1, x1, y1))