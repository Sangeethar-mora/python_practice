# Exercise 1: Perform Basic Set Operations
# Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
# Add Element: Add “grape” to the fruits set.
# Remove Element: Remove “banana” from the fruits set.
# Discard Element: Try to discard “mango” from the fruits set.
# Expected Output:
#
# 1. After creating the set: {'apple', 'orange', 'mango', 'banana'}
# 2. After adding 'grape': {'orange', 'banana', 'grape', 'apple', 'mango'}
# 3. After removing 'banana': {'orange', 'grape', 'apple', 'mango'}
# 4. After discarding 'mango': {'orange', 'grape', 'apple'}

creating_set = {'apple', 'orange', 'mango', 'banana'}
print("After creating the set: ",creating_set)
creating_set.add("grape")
print("After adding 'grape': ",creating_set)
creating_set.remove("banana")
print("After removing 'banana': ",creating_set)
creating_set.discard("mango")
print("After discarding 'mango': ",creating_set)
