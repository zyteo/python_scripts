# this script reads an excel file with 3 columns, then sums up all unique items within columns
import pandas as pd

# open and read file
df = pd.read_excel(open('categorise_sample.xlsx', 'rb'),
              sheet_name='Sheet1', header=None) 

# save df to a list
list = df.to_numpy().tolist()

# create dictionary to store unique items
category = {}

for item in list:
    # if last charater is a space, remove it
    if item[1][-1] == ' ': 
        item[1] = item[1][:-1]
    if item[1] in category:
        category[item[1]] += item[2]
    else:
        category[item[1]] = item[2]

# from dictionary, create a new list
new_list = []

for key, value in category.items():
    new_list.append([key, value])

# create a new dataframe from the new list
new_df = pd.DataFrame(new_list, columns=['Item', 'Cost'])

# save new dataframe to excel file
new_df.to_excel('categorise_output.xlsx', index=False)