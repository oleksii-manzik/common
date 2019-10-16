import math
from string import ascii_lowercase, ascii_letters, punctuation


def common_between_two_lists(list1, list2):
    """Task 1: Returns a list that contains only the elements that are
    common between the lists (without duplicates)"""
    return list(set(list1).intersection(set(list2)))


def count_character(string, character):
    """Task 2: Return the number of times that the letter appears
    anywhere in the given string"""
    return string.count(character)


def is_power_of_three(num):
    """Task 3: Check if a given positive integer is a power of three"""
    return math.log(num, 3).is_integer() if num > 0 else False


def add_until_single_digit(num):
    """Task 4: Add the digits of a positive integer repeatedly until
    the result has a single digit"""
    while len(str(num)) > 1:
        num = sum([int(x) for x in list(str(num))])
    return num


def push_zeros_to_end(input_list):
    """Task 5: Push all zeros to the end of a list"""
    zeros = [x for x in input_list if x == 0]
    result_list = [x for x in input_list if x != 0]
    result_list.extend(zeros)
    return result_list


def is_arithmetic_progression(sequence):
    """Task 6: Check a sequence of numbers is an arithmetic progression
    or not"""
    if len(sequence) < 3:
        return False

    step = sequence[1] - sequence[0]

    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i - 1] != step:
            return False
    else:
        return True


def isnt_occur_twice(input_list):
    """Task 7: Find the number in a list that doesn't occur twice"""
    return [x for x in set(input_list) if input_list.count(x) < 2][0]


def find_missing_num(input_list):
    """Task 8: Find a missing number from a list"""
    check_list = set(range(input_list[0], input_list[-1]))
    return list(check_list.difference(set(input_list)))[0]


def count_until_tuple(input_list):
    """Task 9: Count the elements in a list until an element is a
    tuple"""
    result_list = []
    for x in input_list:
        if isinstance(x, tuple):
            return len(result_list)
        else:
            result_list.append(x)
    else:
        return len(result_list)


def reverse_str(string: str) -> str:
    """Task 10: Take the str parameter being passed and return the
    string in reversed order"""
    return string[::-1]


def convert_to_minutes_seconds(num):
    """Task 11: Take the num parameter being passed and return the
    number of hours and minutes the parameter converts to"""
    return ':'.join([str(num // 60), str(num - (num // 60 * 60))])


def find_largest_word(string):
    """Task 12: Return the largest word in the string"""
    return max([''.join([c for c in x if c not in punctuation])
                for x in string.split()], key=len)


def backwards_order_str():
    """Task 13: Asks the user for a long string containing multiple
    words. Print back to the user the same string, except with the
    words in backwards order."""
    return ' '.join(input().split()[::-1])


def generate_fibonnaci_nums():
    """Task 14: Asks the user how many Fibonnaci numbers to generate
    and then generates them"""
    n = int(input())
    result_list = []
    a, b = 1, 1
    for i in range(n):
        result_list.append(a)
        a, b = b, a + b
    return result_list


def even_nums(input_list):
    """Task 15: Makes a new list that has only the even elements of
    this list in it"""
    return [x for x in input_list if x % 2 == 0]


def add_up_nums():
    """Task 16: Add up all the numbers from 1 to input number"""
    n = int(input())
    return sum(range(n + 1))


def factorial(num):
    """Task 17: Take the parameter being passed and return the
    factorial of it"""
    return math.factorial(num)


def following_letter_capitalize_vowel(string):
    """Task 18: Take the str parameter being passed and modify it using
    the following algorithm. Replace every letter in the string with
    the letter following it in the alphabet (ie. c becomes d, z becomes
    a). Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string."""
    up_one_letters = [ascii_lowercase[ascii_lowercase.index(x) + 1]
                      if x != 'z' else 'a'
                      for x in string]
    return ''.join([x if x not in 'aeiou' else x.upper()
                    for x in up_one_letters])


def sort_alphabetical_order(string):
    """Task 19: Take the str string parameter being passed and return
    the string with the letters in alphabetical order (ie. hello
    becomes ehllo)"""
    return ''.join(sorted([char for char in string if char in ascii_letters]))


def is_num2_greater_num1(num1, num2):
    """Task 20: Take both parameters being passed and return the true
    if num2 is greater than num1, otherwise return the false. If the
    parameter values are equal to each other then return the string
    -1"""
    return False if num1 > num2 else True if num2 > num1 else '-1'
