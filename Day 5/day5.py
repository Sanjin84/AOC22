# Create 9 stacks such that each stack is a dictionary item with string keys 1-9 and a list for a value
stacks = dict()
for i in range(1,10):
    stacks[str(i)] = []

stacks['1'] = ['D','T','R','B','J','L','W','G']
stacks['2'] = ['S','W','C']
stacks['3'] = ['R','Z','T','M']
stacks['4'] = ['D','T','C','H','S','P','V']
stacks['5'] = ['G','P','T','L','D','Z']
stacks['6'] = ['F','B','R','Z','J','Q','C','D']
stacks['7'] = ['S','B','D','J','M','F','T','R']
stacks['8'] = ['L','H','R','B','T','V','M']
stacks['9'] = ['Q','P','D','S','V']

#Create a function called move with parameters num_items, from_stack, to_stack

def move(num_items, from_stack, to_stack):
    global stacks
    #Create a for loop that iterates through the range of num_items
    for i in range(num_items):
        #Pop the last item from the from_stack and append it to the to_stack
        stacks[to_stack].append(stacks[from_stack].pop())

#read the file
with open('input_day5.txt') as f:
    lines = f.readlines()
    #Create a for loop that iterates through the lines in the file
    for line in lines:
        line = line.split()
        print(line)
        #Create a variable called num_items and set it equal to the first item in the list
        num_items = int(line[1])
        #Create a variable called from_stack and set it equal to the second item in the list
        from_stack = line[3]
        #Create a variable called to_stack and set it equal to the third item in the list
        to_stack = line[5]
        #Call the move function with num_items, from_stack, and to_stack as arguments
        move(num_items, from_stack, to_stack)
        for item in stacks:
            print(item, stacks[item])
        print('----------------')