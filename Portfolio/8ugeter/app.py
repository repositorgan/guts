from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# -------- Helper function to parse CSV -------- #
def analyze_csv(csv_file):
  reader = csv.DictReader(csv_file.splitlines())
  income = 0
  expenses = 0
  categories = {}

  for row in reader:
    amount = float(row["amount"])
    category = row["category"].strip()

    if amount > 0:
      income += amount
    else:
      expenses += abs(amount)

    categories[category] = categories.get(category, 0) + abs(amount)

    # Generate insights
  insight = ""
  if expenses > income:
    insight = "Warning: You are spending more than you earn."
  else:
    insight = "Great job! You are spending less than your income."

  top_category = max(categories, key=categories.get)

  return {
    "income": income,
    "expenses": expenses,
    "categories": categories,
    "insight": insight,
    "top_category": top_category,
    }

# -------- Flask Routes -------- #
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
  file = request.files["csv_file"]
  if not file:
    return "No file selected."

    csv_text = file.read().decode("utf-8")
    results = analyze_csv(csv_text)

    return render_template("dashboard.html", data=results)

if __name__ == "__main__":
    app.run(debug=True)
