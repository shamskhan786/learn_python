# #  Question 1
# # "Write a program that calculates the sum of numbers from 1 to 10."


# # One way
# total = sum(range(1,11))
# print(f"The sum of numbers from 1 to 10 is {total}")

# # Second way

# total = 0

# for i in range(1,11):
#     total += i
# print(f"The sum of numbers from 1 to 10 is {total}")


# #  Question 2
# # "Write a program that checks whether the given number is odd or even."

# user_input = int(input("Enter your number:"))

# if user_input % 2 == 0:
#     print(f"{user_input} is even number")
# else:
#     print(f"{user_input} is odd number")    

#  #  Question 3

# # "Write a program that calculates the sum and average of numbers inside a list. Example input: [2, 4, 6, 8, 10]."

# numbers = [1,4,6,8,55]

# sum_of_numvers = sum(numbers)

# avarage = sum_of_numvers / len(numbers)

# print(f"The sum of numbers is {sum_of_numvers} and the avarage is {avarage}")

# #  Question 4

# # Write a program that takes a word and checks whether it is a palindrome (a word that reads the same forward and backward, like 'madam').
# user_word = input("Enter your word:")

# if user_word == user_word[::-1]:
#     print(f"{user_word} is a palindrome")
# else:
#     print(f"{user_word} is not a palindrome")

# #  Question 5

# # Write a program that finds the maximum and minimum numbers in a list.

# list_of_numbers = [34,22,44,66,78,94,22]

# maximum = max(list_of_numbers)
# minimum = min(list_of_numbers)

# print(f"The maximum number is {maximum} and the minimum number is {minimum}")

# #  Question 6

# # Write a program that takes two numbers as input from the user and calculates their product (multiplication)

# number_one = int(input("Enter your first number:"))
# number_two = int(input("Enter your second number:"))

# sum = number_one * number_two
# print(f"The product of {number_one} and {number_two} is {sum}")

# #  Question 7

# # get the input from the user

# user_name = input("Enter your Name:")
# user_age = input("Enter your Age:")

# #print output

# print(f"Hellor {user_name} and You are {user_age} years old")


# #  Question 8

# # Write a program that takes a string and counts the number of vowels (a, e, i, o, u) in it.

# user_input = input(("Enter your string:"))

# vowels = "aeiouAEIOU"

# count = 0
# for word in user_input:
#     if word in vowels:
#         count += 1

# print(f"The number of vowels in the string is {count}")

# #   Question 9

# # Write a program that removes duplicate elements from a list and prints the unique elements.
# #  One way
# #  
# list_of_number = [1,2,3,4,4,5,6,6,7]
# unique_number = list(set(list_of_number))

# print(unique_number)

#  Second way

list_of_number_two = [1,2,3,4,4,5,6,6,7,33,22,22]

empty_list =[]

for num in list_of_number_two:
    if num not in empty_list:
        empty_list.append(num)

print(empty_list)







