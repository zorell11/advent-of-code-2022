# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won

X = 1
Y = 2
Z = 3

scores = {
    "A X" : 3 + X, "B Y" : 3 + Y, "C Z" : 3 + Z, 
    "A Y" : 6 + 2, "B Z" : 6 + Z, "C X" : 6 + X, 
    "A Z" : 0 + 3, "B X" : 0 + X, "C Y" : 0 + 2
}


with open('input', 'r') as f:
    data = f.read().splitlines()

#task1
task1 = 0

for i in data: 
    task1 += scores[i]
    
print(task1)


#task2
new_scores = {
    "A X" : 0 + Z, "B X" : 0 + X, "C X" : 0 + Y, 
    "A Y" : 3 + X, "B Y" : 3 + Y, "C Y" : 3 + Z,
    "A Z" : 6 + Y, "B Z" : 6 + Z, "C Z" : 6 + X
}

task2 = 0

for i in data: 
    task2 += new_scores[i]
    
print(task2)
