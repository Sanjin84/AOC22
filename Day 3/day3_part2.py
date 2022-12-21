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

#group every 3 lines into a tuple and store in processed_data
for i in range(0, len(data), 3):
    processed_data.append((data[i], data[i+1], data[i+2]))
    #if a char exists in all 3 lines, add it to priority_scores
    for c in data[i]:
        if c in data[i+1] and c in data[i+2]:
            #index of c in alphabet
            priority_scores[str(int(i/3) + 1) + ': '+c] = alphabet.index(c)+1

print(processed_data)



#add up all the values in priority_scores
total = 0
for key in priority_scores:
    print(key, priority_scores[key])
    total += priority_scores[key]
print(total)