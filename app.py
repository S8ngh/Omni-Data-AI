import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def analyze(df):
    return df.describe()

if __name__ == "__main__":
    df = load_data("sample_data/sales.csv")
    print(analyze(df))

