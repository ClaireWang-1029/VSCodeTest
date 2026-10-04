#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (mountain+", formerly")
print("known as " +nickname+",")
print ("is " + str(elevation) + "' above sea level." )


#%% Task 2 - Lists and Iteration
data_fld= r"W:\859_data\triangle"
data_list=["streams.shp",
           "stream_types.cvs", "naip_imagery.tif"]
user_item="roads.shp"
data_list.append(user_item)

for filename in data_list:
    print(data_fld+"\\"+filename)
# %% 
user_numbers=[]
for i in range(3):
    number = int(input("Enter an integer:"))
    user_numbers.append(number)

user_numbers.sort()
print(user_numbers[-1])
# %%
user_numbers=[]
for i in range(3):
    number= int(input("Enter an integer:"))
    user_numbers.append(number)

user_numbers.sort(reverse=True)
print(user_numbers)