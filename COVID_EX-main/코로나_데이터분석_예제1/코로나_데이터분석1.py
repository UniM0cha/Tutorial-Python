import pandas as pd
df = pd.read_csv("data/코로나.csv")
df = df.drop(columns = df.columns[[2,3,4,6,7,8,9,10,11]], axis = "columns")
print(df.head())
print(df.info())

import numpy as np
data = np.array(df['Confirmation_date'])
print(data)
confirmation = [0 for i in range(12)]

for row in data :
  date = row.split('-')
  year = date[0]
  month = date[1]
  if year == '2021':
    confirmation[int(month[1]) - 1] += 1

for i in range(4) :
  print( f'2021년 {i + 1}월 확진자 수는 ', confirmation[i], "입니다")
import matplotlib.pyplot as plt
variable = np.array([confirmation[0],confirmation[1],confirmation[2],confirmation[3]])
month = ['1month', '2month', '3month', '4month']
plt.plot(month, variable, label = "confirmation", c = "blue")
plt.title("2021_COVID19")
plt.xlabel("month")
plt.ylabel("confirmation")
plt.legend(loc='best')
plt.show()
