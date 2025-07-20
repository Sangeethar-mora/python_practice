# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:
#
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:
#
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

def slice_list_into_three(sample_list):
    chunk_rev_1 = []
    chunk_1 = sample_list[:3]
    for i in chunk_1[::-1]:
        chunk_rev_1.append(i)
    chunk_rev_2 = []
    chunk_2 = sample_list[3:6]
    for i in chunk_2[::-1]:
        chunk_rev_2.append(i)
    chunk_rev_3 = []
    chunk_3 = sample_list[6:]
    for i in chunk_3[::-1]:
        chunk_rev_3.append(i)
    result = (
        f"Chunk  1 {chunk_1}\nAfter reversing it {chunk_rev_1}\n"
        f"Chunk  2 {chunk_2}\nAfter reversing it {chunk_rev_2}\n"
        f"Chunk  3 {chunk_3}\nAfter reversing it {chunk_rev_3}\nz"
    )
    return result

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(slice_list_into_three(sample_list))


