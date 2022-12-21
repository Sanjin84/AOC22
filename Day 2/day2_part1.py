# A = rock, B = paper, C = scissors
# X = rock, Y = paper, Z = scissors
#1 point for Rock, 2 points for Paper, and 3 points for Scissors
# each round has 6 points for a win, 3 points for a tie, and 0 points for a loss

# read the file input_day2.txt and split each line into a list of strings
with open('input_day2.txt') as f:
    lines = [line.split() for line in f]

my_score =0

#for each line in lines, your opponents move with be the first element in the list and your move will be the second element in the list
for line in lines:
    me = line[1]
    opponent = line[0] 
    # A = rock, B = paper, C = scissors
    # X = rock, Y = paper, Z = scissors
    #1 point for Rock, 2 points for Paper, and 3 points for Scissors
    # each round has 6 points for a win, 3 points for a tie, and 0 points for a loss
    if me == 'X' and opponent == 'A':
        my_score += 3
        my_score += 1
    elif me == 'X' and opponent == 'B':
        my_score += 0
        my_score += 1
    elif me == 'X' and opponent == 'C':
        my_score += 6
        my_score += 1
    elif me == 'Y' and opponent == 'A':
        my_score += 6
        my_score += 2
    elif me == 'Y' and opponent == 'B':
        my_score += 3
        my_score += 2
    elif me == 'Y' and opponent == 'C':
        my_score += 0
        my_score += 2
    elif me == 'Z' and opponent == 'A':
        my_score += 0
        my_score += 3
    elif me == 'Z' and opponent == 'B':
        my_score += 6
        my_score += 3
    elif me == 'Z' and opponent == 'C':
        my_score += 3
        my_score += 3

print(my_score)