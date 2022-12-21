#read file input_day1.txt and store in a list
with open('input_day1.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]


#iterate through data convert each non blank string to integer
for i in range(len(data)):
    if data[i] != '':
        data[i] = int(data[i])

totals = []
#iterate through data and print the sum of numbers between ''
current_total = 0
for number in data:
    if number == '':
        totals.append(current_total)
        current_total = 0
    else:
        current_total += number

print(totals)
first = max(totals)
#remove first from list
totals.remove(first)
second = max(totals)
#remove second from list
totals.remove(second)
third = max(totals)
#remove third from list
totals.remove(third)

print(first+second+third)
