import pandas as pd
import numpy as np

df = pd.read_csv("maalinger.txt", header=None, names=["Values"])
print(df.head())
