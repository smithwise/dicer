import re
from random import randint as dx

def split_input(user_input):
  """
  this splits input by whitespace, and indexes into a list of strings, then returns the list
  :param user_input:
  :return:
  """
  input_tuple = tuple(user_input.split())
  return input_tuple #tuple to maintain input integrity

def validate_input(input_tuple):
  """
  this uses regex to validate proper formatting of input, for now 0dX is an acceptable input
  :param input_tuple:
  :return:
  """
  err = []
  validity = True
  for input_string in input_tuple: # loops through each indexed input
    if re.match(r"^\d+d(4|6|8|10|12|20|100)$", input_string):
        pass
    else:
        err.append(input_string)
  if len(err) > 0:
    validity = False
  return validity, err #returns boolean and list from function

def roll_dice(input):
    

input_seed = input("Input dice to roll in format xdy (xdy ...) \ninput: ")
    #erase string and remove comment mark for prod. Allows user input with prompt
roll_tuple = split_input(input_seed)
    #splits input by whitespace, returns a tuple
valid, error_list = validate_input(roll_tuple) #checks list against regex
    #valid shows if matches allowed regex, and if not delivers list of input that doesnt match
if not valid:
    print(f'You put {input_seed}.\ninput {error_list} does not match regex')

if valid:
    #this only happens if there are no validation errors
    input_string = ""
    returned_value = 0
    results = {} #k=input_string, v=returned_value
    roll_matrix = []
    roll_values = []

    for i in range(len(roll_tuple)):
        for str_in in roll_tuple: #iterate the tuple
            results.update({str_in:0})
            temp_list = str_in.split('d') #splits xdy into [x, y]
            int_list = list(map(int, temp_list)) #converts str in list to int
            roll_matrix.append(int_list) #appends new list to roll_matrix

        for list in roll_matrix: #iterate through lists in matrix
            value=0 #zeros value for each loop of the matrix
            for i in range(int(list[0])): #range should be x
                rand = dx(1, int(list[1])) #(1, y) gives range of y sided die
                value += rand #sums the random numbers iterated
            roll_values.append(value) #add value to the list
        print(roll_values)
