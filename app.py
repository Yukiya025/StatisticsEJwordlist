from flask import Flask, request, render_template
import statsej_func
import os
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # 日本語→英語: 0, 英語→日本語: 1
        form_input = request.form['input']
        jaen = form_input[0:1]
        source = form_input[1:]     
        return render_template('index.html',
                               form_input= source + ": " + statsej_func.search_result(jaen, form_input))
            
        
if __name__ == '__main__':
    app.run(debug=True) 