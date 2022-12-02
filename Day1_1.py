import random

# for each item in list, add sequentially and store as x. If \n, print x reset
# count and start again, output as new line.  

with open('input.txt') as f:
    for line in f:
        x = sum(line)
        if "" in line:
            x = 0
        print(line.strip())

