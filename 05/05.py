from copy import deepcopy

with open('input', 'r') as f:
    data = f.read().split('\n\n')


def rotate(a):
    b = []
    for i in range(len(a[0])):
        b.append([])
    for i in a:
        for j,k in enumerate(i):
            b[j].insert(0,k)
    return b

data[0], number = data[0].split(' 1')


stacks = []
stack = []
for i, j in enumerate(data[0]):
    if j == '\n':
        stacks.append(stack)
        stack = []
    elif i%4 == 1:
        stack.append(j)

stacks = rotate(stacks)

new_stacks = []
for i in range(len(stacks)):
    st = []
    for j in range(len(stacks[0])):
        if stacks[i][j] != ' ':
            st.append(stacks[i][j])
    new_stacks.append(st[:])

task1 = deepcopy(new_stacks)
task2 = deepcopy(new_stacks)


#taks1 + task2
for i in data[1].split('\n'):
    z = list(map(int,i.replace('move','').replace(' from ',' ').replace(' to ',' ').split()))
    y = [] #task2
    for j in range(z[0]):
        x = task1[z[1]-1].pop() #task1
        task1[z[2]-1].append(x) #task1

        y.insert(0, task2[z[1]-1].pop()) #task2
    task2[z[2]-1].extend(y[:])  #task2
        
        

for i in task1:
    print(i[-1], end='')
print()


for i in task2:
    print(i[-1], end='')
print()