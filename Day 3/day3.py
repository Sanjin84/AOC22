#step 1 - read the input file and store the data in a list and remove newline characters
with open('input_day3.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

#print(data)
#step 2 - split each item in the data list into two halves of equal length
processed_data = []
priority_scores =dict()
#create alphabet from a-z and A-Z
alphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
print(alphabet)
line=0
for item in data:
    line += 1
    first = item[:len(item)//2]
    second = item[len(item)//2:]
    processed_data.append((first, second))
    #find char c which exists in both first and second
    for c in first:
        if c in second:
            #index of c in alphabet
            priority_scores[str(line) + ': '+c] = alphabet.index(c)+1
print(priority_scores)

#add up all the values in priority_scores
total = 0
for key in priority_scores:
    print(key, priority_scores[key])
    total += priority_scores[key]
print(total)