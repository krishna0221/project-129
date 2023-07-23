import pandas as pd
import numpy as np
stars = pd.read_csv("/Users/shailendrashukla/Desktop/python/project 128/dwarf_stars.csv")
new_stars = stars.replace(np.nan,"",regex=True)
print(new_stars)
mass_list=[]

for i,j in new_stars.iterrows():
  if j[3]=="":
    mass_list.append(j[3])
    continue
  else:
    j[3]=j[3]*0.000954588
    mass_list.append(j[3])
print(len(mass_list))
new_stars["Solar_Mass"]=mass_list

temp_list=[]
for i,j in new_stars.iterrows():
  if j[4]=="":
    temp_list.append("")
  else:
    print(float(j[4])*0.102763)
    temp_list.append(float(j[4])*0.102763)
new_stars["Solar_Radius"]=temp_list

dd=pd.read_csv("/Users/shailendrashukla/Desktop/python/project 128/bright_stars.csv")
final_list=pd.merge(dd,new_stars,on="id")
final_list.to_csv("final_data.csv")



    