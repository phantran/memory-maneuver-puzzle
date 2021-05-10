## Advent of Code - Memory Maneuver Puzzle

Feel free to use this source code as a template for your coding challenges or puzzles solving 

### Link to puzzle 
https://adventofcode.com/2018/day/8

### Requirements

- Python 3.8

### Usage


`python run.py --im file` <br>

- Use the command above for input data from the text file ***input.txt***. 

- Input data can be changed in ***input.txt***, one numbers list on each line.

- Custom file path can be specified with the argument --f, otherwise input.txt will be used by default.


`python run.py --im cmd --l INPUT_LISTS` <br>

- Use the command above for input data from cmd, replace INPUT_LISTS with the input data of the puzzle. 
  
For example: python run.py --im cmd --l 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2

- For input as multiple numbers lists, use multiple --l arguments

For example: python run.py --im cmd --l 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2 --l 1 3 0 3 10 11 12 1 1 2


This project supports 2 strategies. Use the argument --s to specify the strategy (algorithm) to be used. If --s is not specified, strategy 1 will be used by default.

For example: python run.py --s 2 --im file

The command above uses the strategy 2 with the file input mode.

### Modification

Extend the Strategy class to add a new solution of the puzzle that you are solving.

Extend the DataSource class to add a new type of input source for the puzzle that you are solving.

### Unit test

This project contains only two simple test cases for demonstration purpose

Installing pytest dependencies with the command below

`pip install -r test/requirements.txt` <br>

Execute tests with

`python -m pytest test/`
