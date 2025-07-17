# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
#
# Given:
#
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:
#
# The USA count is: 2

def extract_words(text):
    wrd = ""
    wrd_list = []

    for char in text:
        if char not in [" ", "."]:
            wrd += char
        elif char == " " and wrd:
            wrd_list.append(wrd.lower())
            wrd = ""
    if wrd:
        wrd_list.append(wrd.lower())

    return wrd_list

def count_words(word_list):
    count_wrd = {}
    for word in word_list:
        if word in count_wrd:
            count_wrd[word] += 1
        else:
            count_wrd[word] = 1
    return count_wrd

def print_by_max_list(count_wrd):
    max_list = []

    for val in count_wrd.values():
        max_list.append(val)

    max_list = sorted(max_list, reverse=True)
    # print(max_list)

    for i in max_list:
        for key, val in count_wrd.items():
            if i == val:
                max_list.remove(i)
                print(key, "appear", val, "times")

def final_text(text):
    words = extract_words(text)
    counts = count_words(words)
    print_by_max_list(counts)

text = "Welcome to USA. usa awesome, isn't it?"
final_text(text)
