import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("data/24250201.csv")
    
    print(df.describe())