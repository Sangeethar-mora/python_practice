# Exercise 10: Write a program to count occurrences of all characters within a string
# Given:
#
# str1 = "Apple"
# Expected Outcome:
#
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

def extract_words(str1):
    count = 0
    wrd_list = []
    count_letters = {}
    for i in str1:
        wrd_list.append(i)
    for i in wrd_list:
        if i in count_letters:
            count_letters[i] += 1
        else:
            count_letters[i] = 1
    return count_letters

str1 = "Apple"
result = extract_words(str1)
print(result)
