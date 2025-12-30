import pandas as pd
from eda import auto_eda

df = pd.read_csv("sample_data/sales.csv")

insights = auto_eda(df)

print("AUTO INSIGHTS:")
for k, v in insights.items():
    print(k, ":", v)
