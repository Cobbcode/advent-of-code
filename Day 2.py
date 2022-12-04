# Advent day 2 part 1 
import pandas as pd
import numpy as np
day_2_data = pd.read_csv("Advent day 2.csv",header=None,names=["Strategy"])

# Separate intwo two columns
day_2_data[["Col1","Col2"]] = day_2_data["Strategy"].str.split(" ",expand=True)

# Drop original column
day_2_data = day_2_data.drop("Strategy",axis=1)

# Replace letters with numbers (then this is the score of the shape too
day_2_data = day_2_data.replace({'A': 1, 'B': 2, 'C': 3,'X':1,'Y':2,'Z':3}, regex=True)

# Create set of conditions to meet. Later, if these are true, then the corresponding outcome value is given

conditions = [day_2_data["Col1"] == day_2_data["Col2"], # draw
             (day_2_data["Col1"] == 1) & (day_2_data["Col2"] == 2),  # win
              (day_2_data["Col1"] == 2) & (day_2_data["Col2"] == 3), # win
              (day_2_data["Col1"] == 3) & (day_2_data["Col2"] == 1)  # win
             ]
outcome = [day_2_data["Col2"] + 3, # draw
           day_2_data["Col2"] + 6, # win
           day_2_data["Col2"] + 6, # win
           day_2_data["Col2"] + 6 # win
          ]

# Use numpy select to check if condition is true. If it is, then in a new column "score", get the outcome
# if no conditions true, then the default is just to use column 2 value - aka a loss in the game, just that shape value

day_2_data["score"] = np.select(conditions,outcome,default=day_2_data["Col2"])

# sum
day_2_data["score"].sum()
print(f'Total score with given strategy is: {day_2_data["score"].sum()}')

# Didn't get round to part 2


