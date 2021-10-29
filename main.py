import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df.columns

df.drop(['Unnamed: 0', 'Unnamed: 0.1'],axis=1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

plt.figure(figsize=(10,5))
plt.title("Stars Solar Mass")
plt.bar(name[0:9],mass[0:9])

