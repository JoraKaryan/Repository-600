
import pandas as pd
import numpy as np


#ex-01
dat = pd.DataFrame()

names = np.array(["Nairi", "Vlad", "Jora", "Hayk", "Arthur", "Ruzanna", "Anahit", "Sona", "Liana", "Vlad","Tatev","Salbina"])
surname = np.array(["Hakobyan", "Poghosyan", "Karyan", "Sahakyan", "Mkrtchyan", "Ordyan", "Kirakosyan","Kirakosyan","Varosyan","Harutyunyan","Alaverdyan","Alaverdyan"])
status = np.array(["tutor", "tutor", "Student", "Student", "Student", "Student", "Student","Student","Student","Student","Student","Student"])
age = np.array(["25-30", "25-30", "25-30", "25-30", "25-30","25-30", "25-30","25-30","25-30","25-30","25-30","25-30"])
sex = np.array(["male", "male", "male", "male", "male", "female", "female","female","female","male","female","female"])



dat["names"] = names
dat["surname"] = surname
dat["status"] = status
dat["age"] = age
dat["sex"] = sex
dat.set_index("names", inplace = True)
print(dat)



#ex-02
import os
thisfolder = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(thisfolder, "netflix_titles.csv")

data = pd.read_csv(data)

print((data["release_year"]> 2015) & (data["cast"].str.contains("Kevin Spacey")) | (data["cast"].str.contains("Leonardo DiCaprio")))

