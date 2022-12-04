# Day 1
import pandas as pd
import numpy as np
data = pd.read_csv('aoc_day1.csv', header=None,names=["Calories"],skip_blank_lines=False)

list_dfs = np.split(data, data[data.isnull()].index) 
count_of_calories = sorted(list(map(lambda df: int(df.sum()[0]),df_list)))

# Part 1
print(f"Part 1 count of calories top elf: {count_of_elfs[-1]}")
# Part 2
print(f"Part 2 count of calories top three elfs: {sum(count_of_elfs[-3:])}")

