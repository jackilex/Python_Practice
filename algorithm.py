
# 1 log even numbers from given number
from typing import NewType


def log_even(nums):
    for x in range(0, nums, 2):
        print(x)


# log_even(13)


# 2 Return the largest number present in the given list.

def max_num(li):
    sort_it = sorted(li, reverse=True)
    return sort_it[0]


arr = [3, 1, 17, 5, 6]
arr2 = [2, 3, -2, 99, 100, 2222, 321]
# print(max_num(arr2))


# 3 function that counts the number of vowels in a given string
# if vowel is in string add to total

def vowel_count(str):
    vowel = ("a", "e", "i", "o", "u")
    total = 0
    for v in vowel:
        if v in str.lower():
            total += str.lower().count(v)
    return total


# strs = "I think, therefore I am."
# print(vowel_count(strs))


# 4
# - Return `true` if the given string is a palindrome.

# - Return `false` if the given string is not a palindrome.

def is_palindrom(str):
    rstr = reversed(str)
    nstring = "".join(rstr)
    return str.lower() == nstring.lower()


s = "racecar"
# print(is_palindrom(s))


# 5 In this activity you will be writing
# code to create a function returns the [factorial]


def factorial(num):
    total = 1
    for x in range(1, num+1):
        total *= x
    return total


# print(factorial(0))

# str = "a lannister always pays his debts"


def letter_uppercse(str):
    x = str.split()
    li = []
    for l in x:
        print(l)
        word = list(l)
        word[0] = word[0].upper()
        li.append("".join(word))
    print(li)
    return " ".join(li)


# print(letter_uppercse(str))

# part 07 algo
# 06

def swap_case(str):
    res = ""
    for letter in str:
        if letter == letter.lower():
            res += letter.upper()
        else:
            res += letter.lower()
    return res


# str = "The Price of Greatness Is Responsibility"
# print(swap_case(str))

# part 08 algo
# 07


def reverse(str):
    res = ""
    for x in range(len(str)-1, -1, -1):
        res += str[x]
    return res


# str = "just keep swimming"
# print(reverse(str))


# 08 revere list in place

def list_reverse(list):
    starting = 0
    ending = len(list)-1
    while ending > starting:
        hold = list[starting]
        list[starting] = list[ending]
        list[ending] = hold
        starting += 1
        ending -= 1
    else:
        return list


lis = [1, 2, 3, 4, 5]

# print(list_reverse(lis))


# 09 The look and say sequence can be understood by reading a number
# out loud, digit by digit,
# but first saying the number of times each digit appears in a row

def look_and_say(n):
    dic = {x: n.count(x) for x in str(n)}
    res = (str(val) + key for key, val in dic.items())

    return "".join(res)


# print(look_and_say("5442"))

# 09
# alo
def char_count(n):
    dic = {x: n.count(x) for x in n}
    return dic


# print(char_count("Hello World!"))

def product_Of_Largest_Two(li):
    li.sort(reverse=True)
    return li[0]*li[1]


# print(product_Of_Largest_Two([-10, -5, -2, -15, -1, -33, -88, -100]))

def is_anagram(a, b):
    if len(a) != len(b):
        return False
    x = sorted(a)
    y = sorted(b)
    return "".join(x) == "".join(y)


strA = "tacocat"
strB = "ctatocato"

# print(is_anagram(strA, strB))


# 12 OOP
# 1 any two divisible by 20?

def multiply_Into_20(li):
    for n in li:
        if 20 % n == 0:
            if (20/n) in li:
                return True
    else:
        return False


# print(multiply_Into_20([-2, 5, 50, 2, -10, 18, 20]))


# 2
def zeroes_nd_ones(str):
    for n in str:
        if str.count(n) % 2 == 0:
            pass
        else:
            return False
    else:
        return True


# print(zeroes_nd_ones("11110"))


# 3

arr1 = [12, 13, 20, 51]
arr2 = [8, 14, 40, 41, 43, 50]


# def merge_sorted(arr1, arr2):
#     new_arr = sorted(arr1+arr2)
#     return new_arr


def merge_sorted(arr1, arr2):
    new_arr = sorted(arr1+arr2)
    arr = []

    for i, val in enumerate(new_arr):
        if len(arr) == 0:
            arr.append(val)
        else:
            if arr[i-1] < val:
                arr.append(val)
            else:
                for index, av in enumerate(arr):
                    if val < av:
                        arr.insert(index, val)
    else:
        return arr


# print(merge_sorted(arr1, arr2))

# 13 mvc
def common_element(arrA, arrB):
    included = list(set(arrA) & set(arrB))
    return included[0]


arrA = [1, 9, 8, 7]
arrB = [10, 12, 1, 6, 5]


# print(common_element(arrA, arrB))


# 3
def string_map(string):
    object = {}
    for i, x in enumerate(string):
        if object.get(x):
            object.get(x).append(i)
        else:
            object[x] = [i]
    else:
        return object


# string = "JavaScript rocks!"
# print(string_map(string))


# 14
# 1

def double_triple_map(arr):
    new_arr = [x*2 if x % 2 == 0 else x*3 for x in arr]
    return new_arr


# arr = [1, 2, 3, 4]

# print(double_triple_map(arr))


# 15
