from sklearn.linear_model import LinearRegression

def train_model(df):
    num = df.select_dtypes(include="number")

    X = num.iloc[:, :-1]
    y = num.iloc[:, -1]

    model = LinearRegression()
    model.fit(X, y)

    return "Prediction model trained successfully"
