import pandas as pd

col_list = ["School Code", "School Name","Town","Zip","Number of Students"]
df = pd.read_csv("school_data.csv", usecols=col_list)

town_dict = {}

for index, row in df.iterrows():
    zip = str(row['Zip'])
    if zip in town_dict:
        town_dict[zip]+=row["Number of Students"]
    else:
        town_dict[zip]=row["Number of Students"]

col_list2 = ["Zip","City","Latitude","Longitude"]
df2 = pd.read_csv("school_locations.csv",sep=';', usecols=col_list2)


student_list = []

for index, row in df2.iterrows():
    zip =str(row['Zip'])
    
    if zip in town_dict:
        student_list.append(town_dict[zip])
    else:
        df2.drop(index, inplace=True)

df2['Student Count'] = student_list
print("prepared data:")
print(df2)
print("saving to csv file...")
df2.to_csv(r'prepared_dataset.csv')







        