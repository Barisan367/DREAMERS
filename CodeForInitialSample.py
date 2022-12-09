#Initial DREAM...

import pandas as pd
import numpy as np
import os
import re
import datetime
from ast import literal_eval 
import sys

os.chdir('<C://...PATH FOR WORKING DIRECTORY//...>')

data = pd.read_excel(r'C:\...<PATH FOR INITIAL SAMPLE FILE>...\Sample.xlsx')

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
cnt = 0
for ind in data.index:
    cnt = cnt + 1
    testing_string = str(data['Text1'][ind])
    conversion = int(testing_string, 16)
    print(str(conversion))
    print("number of digits in above number = ",len(str(conversion)))
    print("sum of the digits in above number = ",getSum(conversion))
    print("average of the digits in above number = ",(getSum(conversion)/len(str(conversion))))
    print("===NEXT===")
    txt1 = 'output' + str(cnt) + '.txt'
    sys.stdout = open(txt1,'wt')  
    
