# Print 1-255
# print1To255()
# Print all the integers from 1 to 255. 

def print1to255():
    for x in range(1, 256, 1):
        print(x)


# Print Ints and Sum 0-255
# PrintIntsAndSum0To255()
# Print integers from 0 to 255, and with each integer print the sum so far. 

def PrintIntsAndSum0To255():
    sum = 0
    for x in range(0, 256):
        print(x)
        sum=sum+x
        print(sum)



# Find and Print Max
# printMaxOfList(lst)
# Given an list, find and print its largest element. 

def printMaxOfList(lst):
    max = lst[0]
    for x in range(0, len(lst)):
        print(lst[x])
        if lst[x]>max:
            max=lst[x]
    print("this is max ", max)


# List with Odds
# returnOddsList1To255()
# Create an list with all the odd integers between 1 and 255 (inclusive). 

def returnOddsList1To255():
    oddList=[]
    for x in range(1, 256, 2):
        oddList.append(x)
    print(oddList)

# Greater than Y
# ReturnListCountGreaterThanY(lst, y)
# Given an list and a value Y, count and print the number of list values greater than Y.

def ReturnListCountGreaterThanY(lst, y):
    count = 0
    for x in range(0, len(lst)):
        if lst[x] > y:
            count+=1
    print(count)


# Max, Min, Average
# PrintMaxMinAverageListVals(lst)
# Given an list, print the max, min and average values for that list.

def PrintMaxMinAverageListVals(lst):
    max = lst[0]
    min = lst[0]
    sum = 0
    for x in range(0, len(lst)):
        if lst[x] > max:
            max = lst[x]
        elif lst[x] < min:
            min = lst[x] 
        sum = lst[x] + sum
    average = sum/len(lst)
    print(max, min, average)


# Swap String For List Negative Values
# SwapStringForListNegativeVals(lst)
# Given an list of numbers, replace any negative values with the string 'Dojo'.

def SwapStringForListNegativeVals(lst):
    for x in range(0, len(lst)):
        if lst[x] < 0:
            lst[x] = 'Dojo'
    print(lst)


# Print Odds 1-255
# PrintOdds1To255()
# Print all odd integers from 1 to 255. 

def PrintOdds1To255():
    for x in range(1, 256, 2):
        print(x)

# Iterate and Print List
# PrintListVals(lst)
# Iterate through a given list, printing each value. 

def PrintListVals(lst):
    for x in range(0, len(lst)):
        print(lst[x])

# Get and Print Average
# PrintAverageOfList(lst)
# Analyze an List’s values and print the average. 

def PrintAverageOfList(lst):
    sum = 0
    for x in range(0, len(lst)):
        sum = sum+lst[x]
    print(sum/len(lst))


# Square the Values
# SquareListVals(lst)
# Square each value in a given list, returning that same list with changed values. 

def SquareListVals(lst):
    for x in range(0, len(lst)):
        lst[x] = lst[x] * lst[x]
    print(lst)

# Zero Out Negative Numbers
# ZeroOutListNegativeVals(lst)
# Return the given list, after setting any negative values to zero. 

def ZeroOutListNegativeVals(lst):
    for x in range(0, len(lst)):
        if lst[x] < 0:
            lst[x] = 0
    print(lst)

ZeroOutListNegativeVals([1,-2,3])

# Shift List Values
# ShiftListValsLeft(lst)
# Given an list, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the list

def ShiftListValsLeft(lst):
    for x in range(0, len(lst)-1):
        lst[x] = lst[x+1]
    lst[len(lst)-1] = 0
    print(lst)

ShiftListValsLeft([1,2,3])




