import re
import random
#---------------------------> definitions
def split_input(user_input, *delimiter): #split input into list
    input_list = user_input.split(*delimiter)
    return input_list  

def validate_input(input_list):
    err = []
    validity = True
    for input_string in input_list:  # loops through each indexed input
        if re.match(r"^\d+d(4|6|8|10|12|20|100)$", input_string): #matches xdy, where x is any int and y is one of the 7 die types
            pass
        else:
            err.append(input_string) #logs errant input to list
    if len(err) > 0:
        validity = False
    return validity, err  # returns boolean and list from function

def determine_value(qt, dSize):
    value = 0
    for iter in range(qt):
        r = random.randint(1, dSize)
        value += r
    return value

# -------------------> main
input_seed = input("Input dice to roll in format xdy (xdy ...) \ninput: ") #prompt
results = {}
str_list = split_input(input_seed) #generates list of input items
valid, error_list = validate_input(str_list)  # checks list against regex
    # valid shows if matches allowed regex, and if not delivers list of input that doesnt match
if not valid:
    print(f'You put {input_seed}.\ninput {error_list} does not match regex')

if valid:
    temp_list = []
    int_list = []
    for i in range(len(str_list)): #iter through list, strip 'd' and convert str to int
        temp_list.append(split_input(str_list[i],'d'))
        temp_list[i] = list(map(int, temp_list[i]))
        int_list.append(determine_value(temp_list[i][0],temp_list[i][1]))

    for n in range(len(str_list)):
        results.update({str_list[n]:int_list[n]})
