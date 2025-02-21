import re  #regex, used for input validation
import random

def split_input(user_input):
  #this splits input by whitespace, and indexes into a list of strings, then returns the list
    input_list = user_input.split()
    return input_list

def validate_input(input_list):
  #this uses regex to validate proper formatting of input, for now 0dX is an acceptable input, may remove later
    err = []
    validity = True
    for input_string in input_list: # loops through each indexed input
        if re.match(r"^\d+d(4|6|8|10|12|20|100)$", input_string): pass
          #looks for xdy, x can be any integer (quantity); d is a necessary input; y can be any acceptable dice type
          #acceptable dice types: 4 6 8 10 12 20 100
        else: err.append(input_string) #appends all errant inputs to list
    if len(err) > 0:
        validity = False
    return validity, err #returns boolean and list from function

# ----------> base seed, remove for prod
input_seed = "1d4 2d6 3d8 4d10 5d12 6d20 7d100" #pre-assigned for testing. will be input in prod:
# input_seed = input("Input dice to roll in format xdy (xdy ...) \ninput: ")

# ----------> main function
roll_list = split_input(input_seed) #base seed used
valid, error_list = validate_input(roll_list)
if not valid:
    print(f'input {error_list} does not match regex')

# print("You rolled " + input_seed) #used for console input testing
