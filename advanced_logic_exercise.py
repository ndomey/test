# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:

sorted_list = sorted(numbers)

delta_number = sorted_list[len(sorted_list) - 1] - sorted_list[0]
print(delta_number)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

num_1 = 0
num_2 = 0

for number in numbers:
    number = num_1
    if num_1 == num_2:
        print(True)

    if number == 2:
        number = num_2
    else:
        break


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# sum = True
# sum_of_num = 0

# for number in numbers:
#     if sum == True:
#         if number == 6:
#             sum = False
#         else:
#             sum_of_num += number
#     else:
#         if number == 7:
#             sum = True
# print(sum_of_num)


adding = True
sum_of_num = 0

for number in numbers:

    if number == 6:
        adding = False
    elif number == 7:
        adding = True

    if number != 6 and number != 7 and adding == True:
        sum_of_num += number
        
print(sum_of_num)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
sum = 0
counter = -1

for number in numbers:
    counter += 1
    
    if number == 13:
        numbers.pop(counter)
        numbers.pop(counter)

for number in numbers:
    sum += number

print(sum)







