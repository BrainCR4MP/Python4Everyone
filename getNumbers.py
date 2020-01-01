#import regular expressions
import re

sum = 0
#make connection to a file (handle)
handle = open("regex_sum_311433.txt")

#read file line by line.
for line in handle:
    #store number that you find on line
    numbers = re.findall('[0-9]+', line)
    #if there is no numbers, continue to next line
    if not numbers:
        continue

    else:
        #go through numbers one by one stored in "numbers" variable
        for value in numbers:
            #take that "value" and add(sum) it to "sum" variable
            sum += int(value)
print(sum)



