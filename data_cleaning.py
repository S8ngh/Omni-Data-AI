def clean_data(df):
    df = df.drop_duplicates()

    for col in df.select_dtypes(include="number").columns:
        df[col].fillna(df[col].mean(), inplace=True)

    for col in df.select_dtypes(include="object").columns:
        df[col].fillna("Unknown", inplace=True)

    return df
