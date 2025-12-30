def answer_question(df, question):
    q = question.lower()

    if "highest" in q:
        col = df.select_dtypes(include="number").columns[0]
        return f"Highest {col} is {df[col].max()}"

    if "average" in q:
        col = df.select_dtypes(include="number").columns[0]
        return f"Average {col} is {df[col].mean()}"

    return "Question understood, feature coming soon!"
