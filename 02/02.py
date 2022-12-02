# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won

X = 1
Y = 2
Z = 3

lose = 0
draw = 3
win = 6 

scores = {
    "A X" : draw + X, "B Y" : draw + Y, "C Z" : draw + Z, 
    "A Y" : win + Y, "B Z" : win + Z, "C X" : win + X, 
    "A Z" : lose + Z, "B X" : lose + X, "C Y" : lose + Y
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
    "A X" : lose + Z, "B X" : lose + X, "C X" : lose + Y, 
    "A Y" : draw + X, "B Y" : draw + Y, "C Y" : draw + Z,
    "A Z" : win + Y, "B Z" : win + Z, "C Z" : win + X
}

task2 = 0

for i in data: 
    task2 += new_scores[i]
    
print(task2)
