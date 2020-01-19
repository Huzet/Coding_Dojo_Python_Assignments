# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(x):
#     for i in range(0,len(x), 1):
#         if x[i] > 0:
#             x[i] = "big"
#     return(x)

# print(biggie_size([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

#     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


# def count_positives(lst):
#     count = 0
#     for x in range(0, len(lst), 1):
#         if lst[x]>0:
#             count = count + 1
#     lst[len(lst)-1] = count
#     return lst

# print(count_positives([1,6,-4,-2,-7,-2]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#     Example: sum_total([1,2,3,4]) should return 10
#     Example: sum_total([6,3,-2]) should return 7

# def sum_total(lst):
#     sum = 0
#     for i in range(0, len(lst)):
#         sum = sum + lst[i]
#     return sum

# print(sum_total([1,2,3,4]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
#     Example: average([1,2,3,4]) should return 2.5

# def average(lst):
#     average = 0
#     for i in range(0, len(lst)):
#         average = average + lst[i]
#     return average/len(lst)

# print(average([1,2,3,4]))

# 5. Length - Create a function that takes a list and returns the length of the list.
#     Example: length([37,2,1,-9]) should return 4
#     Example: length([]) should return 0

# def length(lst):
#     length = len(lst)
#     return length

# print(length([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
    # Example: minimum([37,2,1,-9]) should return -9
    # Example: minimum([]) should return False

# def minimum(lst):
#     if len(lst) == 0:
#         return 'false'
#     min = lst[0]
#     for i in range(1, len(lst)):
#         if min > lst[i]:
#             min = lst[i]
#     return min

# print(minimum([37,2,1,-9]))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#     Example: maximum([37,2,1,-9]) should return 37
#     Example: maximum([]) should return False

# def maximum(lst):
#     if len(lst) ==0:
#         return 'false'
#     max = lst[0]
#     for i in range(1,len(lst)):
#         if max < lst[i]:
#             max = lst[i]
#     return max

# print(maximum([]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#     Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(lst):
#     myDict = {}
#     total = 0
#     minimum = lst[0]
#     maximum = lst[0]
#     for i in range(0, len(lst)):
#         total = total + lst[i]
#         if maximum < lst[i]:
#             maximum = lst[i]
#         elif minimum > lst[i]:
#             minimum = lst[i]
#     myDict['sumTotal'] = total
#     myDict['average'] = total/len(lst)
#     myDict['minimum'] = minimum
#     myDict['maximum'] = maximum
#     myDict['length'] = len(lst)
#     return myDict

# print(ultimate_analysis([37,2,1,-9]))

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(lst):
    temp = 0
    leng = round(len(lst) /2 )
    for i in range(0, leng, 1):
        temp = lst[i] 
        lst[i] = lst[len(lst)-1 -i]
        lst[len(lst)-1 -i] = temp
    return lst


print(reverse_list([37,2,1,-9,2]))
    





