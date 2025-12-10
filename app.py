from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime

app = Flask(__name__)

FILE_NAME = "expenses.csv"

# Create CSV if not exists
try:
    pd.read_csv(FILE_NAME)
except:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)


@app.route("/")
def index():
    df = pd.read_csv(FILE_NAME)

    total_expense = df["Amount"].sum()

    category_summary = df.groupby("Category")["Amount"].sum().to_dict()

    insights = generate_insights(df)

    return render_template(
        "index.html",
        total=total_expense,
        categories=category_summary,
        insights=insights
    )


@app.route("/add", methods=["POST"])
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = request.form["category"]
    amount = float(request.form["amount"])
    description = request.form["description"]

    df = pd.read_csv(FILE_NAME)
    new_entry = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    return redirect("/")


def generate_insights(df):
    insights = []

    if df.empty:
        insights.append("Start adding expenses to get AI insights!")
        return insights

    avg_spending = df.groupby("Category")["Amount"].mean()

    for category, avg in avg_spending.items():
        if avg > 3000:
            insights.append(
                f"You are spending heavily on {category}. Consider setting a budget."
            )

    highest = df.groupby("Category")["Amount"].sum().idxmax()
    insights.append(f"Your highest spending is on {highest} category.")

    return insights


if __name__ == "__main__":
    app.run(debug=True)
