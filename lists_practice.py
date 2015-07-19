# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, -20]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    #what is the space and time?

    odd_list =[]
    for item in number_list:
        if item % 2 != 0:
            odd_list.append(item)
    
    #oddlist = [item for item in number_list if item % 2 != 0]
    return odd_list

#print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    #what is the space and time?

    # even_list =[]
    # for item in number_list:
    #     if item % 2 == 0:
    #         even_list.append(item)
    even_list = [item for item in number_list if item % 2 == 0]
    return even_list

#print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    #what is the space and time?

    # long_words_list = []
    # for word in word_list:
    #     if len(word) >= 4:
    #         long_words_list.append(word)
    long_words_list = [word for word in word_list if len(word) >= 4]
    return long_words_list

#print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    #what is the space and time?

    small = number_list[0]
    for numb in number_list:
        if numb < small:
            small = numb

    return small
#print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    #what is the space and time?

    large = number_list[0]
    for numb in number_list:
        if numb > large:
            large = numb

    return large
# print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):

    #what is the space and time?

    # divided_list = []
    # for numb in number_list:
    #     half = float(numb) / 2.0
    #     divided_list.append(half)
    divided_list = [(float(numb)/2) for numb in number_list]
    return divided_list
#print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = [len(word) for word in word_list]
    return length_list

# print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
#space and time?

    sum_of_all_numbers = 0
    for numb in number_list:
        sum_of_all_numbers += numb
    return sum_of_all_numbers
# print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):

#space and time?

    prod_of_all_numbers = 1
    for numb in number_list:
        prod_of_all_numbers *= numb
    return prod_of_all_numbers

# print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):

    # unpack list into strings by iterating over list using slice and add those strings together
    new_string = ""
    for word in word_list:
        new_string = new_string + word
    return new_string

# print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    # go through list and add each one to each other -- use our sum function?
    # divide sum by len(number_list)
    list_avg = float(sum_numbers(number_list)) / len(number_list)
    return list_avg