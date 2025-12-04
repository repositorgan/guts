from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("csv_file")

    if not file:
        return "No file uploaded.", 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading CSV: {e}", 400

    summary = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "preview": df.head().to_html(classes="table", index=False)
    }

    return render_template("results.html", summary=summary)

if __name__ == "__main__":
    # debug=True auto-refreshes changes
    app.run(host="0.0.0.0", port=5000, debug=True)
