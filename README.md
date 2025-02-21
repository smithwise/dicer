# dicer
Simple Dice Rolling to practice python, and for import into other DND related repos

Stage 1: Receive and validate user input.
* 1.1: prompt user input, store in variable
* 1.2: split input to allow complex statements (i.e. 1d4 3d10 2d6)
* 1.3: validate input using regex

Stage 2: return appropriate random values based on validated user input.
* 2.1: split input list further into k:v pairs to aid computation
* 2.2: define function to return product of dSize * qt (key * value)
* 2.3: <rule of three, find another step>

Stage 3: Simplify and ready code to be called by other files.
* boil down into class and function definitions.
