from flask import Flask,request,render_template

app=Flask(__name__)

import math
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/cel',methods=['GET','POST'])
def covert():
    value ="Invalid"
    if request.method=='POST':
        cel=int(request.form['cel'])
        value=(cel * 9/5) + 32
        result=f"{cel}°C is equal to {value}°F"
    return render_template('index.html',value=result)
    

if __name__=='__main__':
    app.run(debug=True)