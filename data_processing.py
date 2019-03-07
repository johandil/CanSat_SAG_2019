import pandas as pd
import numpy as np

df = pd.read_csv("datatry.txt", header=None, names=["Values"])
print(df.head())
