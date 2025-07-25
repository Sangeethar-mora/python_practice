# Exercise 7: Count Occurrences
# Count and print how many times 'Football' appears in list.
#
# Given:
#
# sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis'].

def count_occurrences(sports):
    return f"Occurrences of Football:  {sports.count("Football")}"
sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print(count_occurrences(sports))
