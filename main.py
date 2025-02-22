import re
import random
#---------------------------> definitions
def split_input(user_input, *delimiter):
    input_list = user_input.split(*delimiter)
    return input_list  # tuple to maintain input integrity

def validate_input(input_list):
    err = []
    validity = True
    for input_string in input_list:  # loops through each indexed input
        if re.match(r"^0+d(4|6|8|10|12|20|100)$", input_string):
            err.append(input_string)
        elif re.match(r"^\d+d(4|6|8|10|12|20|100)$", input_string):
            pass
        else:
            err.append(input_string)
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
valid, error_list = validate_input(str_list)  # checks input list against regex

valid_list = [x for x in str_list if x not in error_list ]

temp_list = []
int_list = []
for i in range(len(valid_list)): #iter through list, strip 'd' and convert str to int
    temp_list.append(split_input(valid_list[i],'d'))
    temp_list[i] = list(map(int, temp_list[i]))
    int_list.append(determine_value(temp_list[i][0],temp_list[i][1]))

for n in range(len(valid_list)):
    results.update({valid_list[n]:int_list[n]})

#print statements below for troubleshooting
print(results)
print()

if not valid:
    print(f'ERROR: \ninput:{input_seed}.\n the following items do not match required format: {error_list}')
