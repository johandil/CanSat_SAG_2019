import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("maalinger.txt", header=None, names=["Temperature", "Humidity"])

df = df.drop(df[df["Temperature"] < -50].index)  # remove readings with temperature below -50
df = df.drop(df[df["Humidity"] < -50].index)  # remove reading with humidity below -50

plt.plot(df["Temperature"])  # plot temperature
plt.plot(df["Humidity"])  # plot humidity
plt.legend()  # plot legend
plt.show()  # show graph


