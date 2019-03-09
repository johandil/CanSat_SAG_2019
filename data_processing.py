import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("maalinger.txt", header=None, names=["Temperature", "Humidity"])
print(df.head())
plt.plot(df["Temperature"])
plt.plot(df["Humidity"])
plt.show()

