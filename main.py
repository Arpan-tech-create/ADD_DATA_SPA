from flask import Flask, request, render_template,jsonify
import sqlite3

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.form
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO table_name (column1, column2) VALUES (?, ?)', (data['column1'], data['column2']))
    conn.commit()
    conn.close()
    return ''

if __name__ == '__main__':
    app.run(debug=True)
