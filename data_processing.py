import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("maalinger.txt", header=None, names=["Temperature", "Humidity"])

for i in range(len(df)):
    if df.loc[i, "Temperature"] < -100 or df.loc[i, "Humidity"] < -100:
        df = df.drop([i], axis=0)

plt.plot(df["Temperature"])
plt.plot(df["Humidity"])
plt.legend()
plt.show()


