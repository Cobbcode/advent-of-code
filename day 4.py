import pandas as pd
data = pd.read_csv("aoc_day4.txt",delimiter = ",",header=None,names=["Assign1","Assign2"])

def format_data(colname):
    output_data = data[colname].str.split("-",expand=True)
    output_data.columns = ["num1","num2"]
    output_data["num1"] = output_data["num1"].astype(int)
    output_data["num2"] = output_data["num2"].astype(int)
    output_data["range"] = [list(range(i, j+1)) for i, j in output_data[["num1","num2"]].values]
    return output_data

assignment1 = format_data("Assign1")
assignment2 = format_data("Assign2")

count = 0
for i in range(0,len(assignment1)):
    if set(assignment1["range"][i]).issubset(assignment2["range"][i]) or set(assignment2["range"][i]).issubset(assignment1["range"][i]):
        count+=1
           
count

# Part 2 
count2 = 0
for i in range(0,len(assignment1)):
    for number in assignment2["range"][i]:
        if number in assignment1["range"][i]:
            count2+=1
            break

count2
