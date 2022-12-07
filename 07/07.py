fs = {}
stack = []

for line in open(0):
    act = line.split()
    if act[1] == 'cd' and act[2] != '..':
        if act[2] == '/':
            x = '/'
            stack.append(x)
        else:
            x = "".join(stack[-1]) + act[2]  + "/"
            stack.append(x)
        fs[x] = 0

    elif act[0].isnumeric():
        for i in stack:
            fs[i] += int(act[0])
    elif act[1] == 'cd' and act[2] == '..':
        stack.pop()


#Task1
size = 0
for i in fs.values():
    if i < 100000:
        size += i
print(size)

#task2
threshold = fs['/'] -( 70000000 - 30000000)
fs = dict(sorted(fs.items(), key=lambda x:x[1]))

for val in fs.values():
    if val > threshold:
        print(val)
        break
