
import pandas as pd
from data_cleaning import clean_data
from eda import auto_eda
from question_ai import answer_question
from model import train_model

df = pd.read_csv("sample_data/sales.csv")

df = clean_data(df)
insights = auto_eda(df)

print(answer_question(df, "highest value"))
print(train_model(df))
