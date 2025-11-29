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

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        # Show the upload page
        return render_template("upload.html")

    # POST = User submitted file
    file = request.files.get("csv_file")

    if file is None or file.filename == "":
        return render_template(
            "upload.html",
            error="No file selected. Please choose a CSV file."
        )

    try:
        df = pd.read_csv(file)

        # Basic summary analysis
        summary = df.describe(include="all").to_html(classes="table table-bordered")

        return render_template(
            "results.html",
            tables=[summary],
            titles=["Uploaded CSV Summary"]
        )

    except Exception as e:
        return render_template(
            "upload.html",
            error=f"Error reading CSV: {str(e)}"
        )
