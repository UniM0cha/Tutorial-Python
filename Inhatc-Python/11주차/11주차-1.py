import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./Inhatc-Python/11주차/data.csv')

df = df.fillna(0)

missing_value = df.isna()
missing_value_sum = missing_value.sum()
print(missing_value_sum)

passenger = df.iloc[:, 0]   # 인덱스로 가져오기
passenger = np.array(passenger, dtype=int)
woman = df.loc[:, "woman"]  # 컬럼명으로 가져오기
woman = np.array(woman, dtype=int)
young = df["young"]
young = np.array(young, dtype=int)
print(passenger)

passenger = pd.DataFrame(passenger.reshape(7, 24))
woman = pd.DataFrame(woman.reshape(7, 24))
young = pd.DataFrame(young.reshape(7, 24))
print(passenger.describe())

