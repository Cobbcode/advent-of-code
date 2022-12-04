import pandas as pd
rucksack = pd.read_csv("aoc_day3.txt",names=["Rucksack"])

# Split column by half
rucksack["split_index"] = rucksack["Rucksack"].str.len()//2

# # Anon function within an apply - for each row, slice by the row's split_index number. convert to lists
compartment1 = rucksack.apply(lambda row: row["Rucksack"][0:row['split_index']],axis=1).to_list()
compartment2 = rucksack.apply(lambda row: row["Rucksack"][row['split_index']:],axis=1).to_list()

# Create dictionary with alphabet lowercase and uppercase, add scores to each letter
import string
letters = dict.fromkeys(string.ascii_lowercase, 0) | dict.fromkeys(string.ascii_uppercase,0)
for index,letter in enumerate(letters):
    letters[letter] = index+1

# Iterate through list item and letters
duplicates = []
for index, phrase in enumerate(compartment1):
    for letter in phrase:
        if letter in compartment2[index]:
            duplicates.append(letter)
            break

def get_sum_of_letters(list):
    for i in range(0,len(list)):
        list[i] = letters[list[i]]
    return sum(list)
        
print(f"Sum of letters part 1: {get_sum_of_letters(duplicates)}")

# PART TWO
rucksack_list = rucksack["Rucksack"].to_list()
split_list = []
for i in range(0, len(rucksack_list), 3):
    split_list.append(rucksack_list[i:i + 3])
    
duplicates_part_two = []
for array in split_list:
    for letter in array[0]:
        if letter in array[1] and letter in array[2]:
            duplicates_part_two.append(letter)
            break

print(f"Sum of letters part 1: {get_sum_of_letters(duplicates_part_two)}")
