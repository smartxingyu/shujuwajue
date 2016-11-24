import numpy as np
dict_all={}
for i in range(10):
    dict_all[i]=i+1
count=0
for key in dict_all.keys():
    count+=dict_all[key]
    count_1 = {i: 0 for i in dict_all.keys}
print(count_1)


