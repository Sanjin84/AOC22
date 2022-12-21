#write a function that reads an input string and returns the index of first 4 non repeating characters
def start_marker(input_string):
    #read input string 4 characters at a time and return the index of first 4 non repeating characters
    #if there are no 4 non repeating characters return -1
    for i in range(len(input_string)):
        segment = input_string[i:i+4]
        #check if segment has 4 non repeating characters
        if len(set(segment)) == 4:
            return i+4
    return None

#read the input_day6.txt file
with open('input_day6.txt') as f:
    input_string = f.read()
    print(start_marker(input_string))