# Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
#
# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:
#
# Emma appeared 2 times


str_x = "Emma is good developer. Emma is a writer"

wrd = ""

wrd_list = []

for i in str_x:
    if i not in [" ", "."]:
        wrd += i
    if i == " ":
        wrd_list.append(wrd.lower())
        wrd = ""
if wrd:
    wrd_list.append(wrd.lower())
    wrd = ""
print(wrd_list)

count_wrd = {}

for i in wrd_list:
    if i in count_wrd:
        count_wrd[i] += 1
    if i not in count_wrd:
        count_wrd[i] = 1

print(count_wrd)

max_list = []

for i in count_wrd:
    max_list.append(count_wrd[i])

max_list = sorted(max_list,reverse=True)
print(max_list)

for i in max_list:
    for key,val in count_wrd.items():
        if i == val:
            max_list.remove(i)
            print(key,"appear",val,"times")

################## using functions #################

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
    print(max_list)

    for i in max_list:
        for key, val in count_wrd.items():
            if i == val:
                max_list.remove(i)
                print(key, "appear", val, "times")

def process_text(text):
    words = extract_words(text)
    counts = count_words(words)
    print_by_max_list(counts)

text = "Emma is good developer. Emma is a writer"
process_text(text)

