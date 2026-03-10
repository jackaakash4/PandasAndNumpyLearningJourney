import pandas as pd

name = ["Aakash", "Shrestha", "Jack"]
deg = ["BScCSIT", "BCA", "MScCSIT"]
score = [90, 100, 100]
data = {
        "Name": name,
        "Degre": deg,
        "Score": score
        }
df = pd.DataFrame(data)
print(df)

#exporting to a working directory
df.to_csv("file1.csv")


#checking if export successed or not
checkdf = pd.read_csv("file1.csv")
print(checkdf)

#if we don't want the index and header in our csv file then we can change it by
#df.to_csv("file1.csv", header = False, index = False)

#if we want to add separation
#use can use /t 

df.to_csv("separate.csv", sep = "\t", index = False)
separate = pd.read_csv("separate.csv", sep="\t")
print("Separate with /t \n", separate) 
