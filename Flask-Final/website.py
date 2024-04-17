from flask import Flask, render_template
from database import get_data
import pandas as pd
app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route('/dataset')
def dataset():
    return render_template('database.html', dataset=dataset)

csv_file_path = r'Credit card transactions_India_Simple.csv'
df = pd.read_csv(csv_file_path)
dataset = df.to_dict(orient='records')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/project_description')
def project():
    return render_template('project_description.html')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
