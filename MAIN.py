#LETS START DREAMING....

import pandas as pd
import numpy as np
import os
import re
import datetime
from ast import literal_eval 
import sys
import statistics 

os.chdir('<PATH FOR THE WORKING DIRECTORY>...//MyCode')

data = pd.read_csv(r'<PATH TO ACCESS THE PRIMARY DATA>...\TrainingData.csv')

data = data.head(40000)

data.insert(3, column = "decimal_equivalent_length", value = "")
data.insert(4, column = "digits_sum_decimal_equivalent", value = "")
data.insert(5, column = "digits_mean_decimal_equivalent", value = "")
data.insert(6, column = "class_detected_programatically", value = "")

df0 = pd.DataFrame(columns = ['SerialCount', 'digits_sum', 'digits_mean'])
df1 = pd.DataFrame(columns = ['SerialCount', 'digits_sum', 'digits_mean'])
df2 = pd.DataFrame(columns = ['SerialCount', 'digits_sum', 'digits_mean'])
df3 = pd.DataFrame(columns = ['SerialCount', 'digits_sum', 'digits_mean'])

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0

for ind in data.index:
    #cnt = cnt + 1
    hexa_string = str(data['Text'][ind])
    conversion = int(hexa_string, 16)
    len_cnt = len(str(conversion))
    sum_cnt = getSum(conversion)
    avg_cnt = (sum_cnt/len_cnt)

    data['decimal_equivalent_length'][ind] = len_cnt
    data['digits_sum_decimal_equivalent'][ind] = sum_cnt
    data['digits_mean_decimal_equivalent'][ind] = avg_cnt

    if data['class'][ind] == 0:
        #df0['class_detected_programatically'][ind] = str(0)
        df0 = df0.append({'SerialCount' : cnt0, 'digits_sum' : sum_cnt, 'digits_mean' : avg_cnt}, 
                ignore_index = True)
        cnt0 = cnt0 + 1
    elif data['class'][ind] == 1:
        #df0['class_detected_programatically'][ind] = str(0)
        df1 = df1.append({'SerialCount' : cnt1, 'digits_sum' : sum_cnt, 'digits_mean' : avg_cnt}, 
                ignore_index = True)
        cnt1 = cnt1 + 1
    elif data['class'][ind] == 2:
        #df0['class_detected_programatically'][ind] = str(0)
        df2 = df2.append({'SerialCount' : cnt2, 'digits_sum' : sum_cnt, 'digits_mean' : avg_cnt}, 
                ignore_index = True)
        cnt2 = cnt2 + 1
    elif data['class'][ind] == 3:
        #df0['class_detected_programatically'][ind] = str(0)
        df3 = df3.append({'SerialCount' : cnt3, 'digits_sum' : sum_cnt, 'digits_mean' : avg_cnt}, 
                ignore_index = True)
        cnt3 = cnt3 + 1

(df0.head(5)).to_csv("Top20_Check.csv",index=False)    

max_0_sum = max(list(df0["digits_sum"])) 
min_0_sum = min(list(df0["digits_sum"]))
max_0_avg = max(list(df0["digits_mean"]))
min_0_avg = min(list(df0["digits_mean"]))

sd_sum_0 = df0['digits_sum'].std()

vr_sum_0 = df0["digits_sum"].var()

sd_avg_0 = df0['digits_mean'].std()
vr_avg_0 = df0['digits_mean'].var()

max_1 = df1.max()
min_1 = df1.min()

sd_sum_1 = df1['digits_sum'].std()
vr_sum_1 = df1['digits_sum'].var()
max_1_sum = max(list(df1["digits_sum"])) 
min_1_sum = min(list(df1["digits_sum"]))
max_1_avg = max(list(df1["digits_mean"]))
min_1_avg = min(list(df1["digits_mean"]))

sd_avg_1 = df1['digits_mean'].std()
vr_avg_1 = df1['digits_mean'].var()

max_2 = df2.max()
min_2 = df2.min()

sd_sum_2 = df2['digits_sum'].std()
vr_sum_2 = df2['digits_sum'].var()
max_2_sum = max(list(df2["digits_sum"])) 
min_2_sum = min(list(df2["digits_sum"]))
max_2_avg = max(list(df2["digits_mean"]))
min_2_avg = min(list(df2["digits_mean"]))

sd_avg_2 = df2['digits_mean'].std()
vr_avg_2 = df2['digits_mean'].var()

max_3 = df3.max()
min_3 = df3.min()

sd_sum_3 = df3['digits_sum'].std()
vr_sum_3 = df3['digits_sum'].var()
max_3_sum = max(list(df3["digits_sum"])) 
min_3_sum = min(list(df3["digits_sum"]))
max_3_avg = max(list(df3["digits_mean"]))
min_3_avg = min(list(df3["digits_mean"]))

sd_avg_3 = df3['digits_mean'].std()
vr_avg_3 = df3['digits_mean'].var()

for ind in data.index:
    sum1 = (data['digits_sum_decimal_equivalent'][ind])
    avg1 = (data['digits_mean_decimal_equivalent'][ind])
    #if (avg1 >= min_0_avg and avg1 <= max_0_avg) and (sum1 <= max_0_sum and sum1 >= min_0_sum): #and (sd_sum_0 <= (2) and sd_sum_0 >= (-2)) and (sd_avg_0 <= (2) and sd_avg_0 >= (-2)):
    if data['decimal_equivalent_length'][ind] == 0:
        data['class_detected_programatically'][ind] = 0
    
    #if (avg1 >= min_1_avg and avg1 <= max_1_avg) and (sum1 <= max_1_sum and sum1 >= min_1_sum): #and (sd_sum_1 <= (2) and sd_sum_1 >= (-2)) and (sd_avg_1 <= (2) and sd_avg_1 >= (-2)):
    if (avg1 >= (4.48) and avg1 <= (4.53)) and (sum1 <= max_1_sum and sum1 >= min_1_sum):
        data['class_detected_programatically'][ind] = 1
    
    #if (avg1 >= min_2_avg and avg1 <= max_2_avg) and (sum1 <= max_2_sum and sum1 >= min_2_sum): #and (sd_sum_2 <= (2) and sd_sum_2 >= (-2)) and (sd_avg_2 <= (2) and sd_avg_2 >= (-2)):
    if (avg1 >= (4.31) and avg1 <= (4.46)) and (sum1 <= max_2_sum and sum1 >= min_2_sum):
        data['class_detected_programatically'][ind] = 2
    
    #if (avg1 >= min_3_avg and avg1 <= max_3_avg) and (sum1 <= max_3_sum and sum1 >= min_3_sum): #and (sd_sum_3 <= (2) and sd_sum_3 >= (-2)) and (sd_avg_3 <= (2) and sd_avg_3 >= (-2)):
    if (avg1 >= (4.45) and avg1 <= (4.57)) and (sum1 <= max_3_sum and sum1 >= min_3_sum):
        data['class_detected_programatically'][ind] = 3

data_top20 = data.head(20)
data_bottom20 = data.tail(20)
data_top20.to_csv("Top20_Check.csv",index=False)
data_bottom20.to_csv("Bottom20_Check.csv",index=False)
