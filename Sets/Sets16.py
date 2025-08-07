# Exercise 16: Count Unique Words
# Write a code to count the number of unique words in the given a sentence.
#
# Given:
#
# sentence = "dog is a simple animal dogs is selfless animal"
# Expected Output:
#
# Number of unique words: 7

sentence = "dog is a simple animal dogs is selfless animal"

list_words = sentence.split()
uni_word = set(list_words)
print("Number of unique words: ",len(uni_word))

