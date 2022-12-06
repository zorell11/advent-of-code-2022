with open('input', 'r') as f:
    data = f.read()

#task1-4 & task2-14
for x in [4,14]:
    for i in range(len(data)):
        if len(set(data[i:i+x])) == x:
            print(i+x)
            break