from flask import Flask, render_template
from data_loader import load_data

app = Flask(__name__)

@app.route('/')
def dashboard():
data = load_data()
return render_template('dashboard.html', data=data)

if __name__ == '__main__':
app.run(debug=True)
