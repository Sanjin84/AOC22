#read the text file input_day4.txt line by line and store it in a list
with open('input_day4.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


#split each item in lines into a tuple, split on the , and store it in a list
lines = [x.split(',') for x in lines]

#for each item in lines, split both items into a list of two items, split on the - and store it in a list
ranges = dict()

for i in range(len(lines)):
    range1 = lines[i][0].split('-')
    range2 = lines[i][1].split('-')
    #convert each item in range 1 and 2 to an integer
    range1 = [int(x) for x in range1]
    range2 = [int(x) for x in range2]

    ranges[str(i+1)] = (range1, range2)

print(ranges)
count = 0
for value in ranges.values():
    bottom1 = value[0][0]
    top1 = value[0][1]
    bottom2 = value[1][0]
    top2 = value[1][1]
    if bottom1 <= bottom2 and top1 >= top2:
        count += 1
    elif bottom2 <= bottom1 and top2 >= top1:
        count += 1


print(count)