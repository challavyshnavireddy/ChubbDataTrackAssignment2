from flask import Flask,request,render_template

app=Flask(__name__)

import math
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/cal',methods=['GET','POST'])
def scal():
    value ="Invalid"
    if request.method=='POST':
        n1=int(request.form['n1'])
        n2=int(request.form['n2'])
        op=request.form['op']
        
        if op=='+':
            value= n1+n2
        elif op=='-':
            value= n1-n2
        elif op=='*':
            value=n1*n2
        elif op=='%':
            value= n1%n2
        elif op == '/':
            value= n1 / n2 if n2 != 0 else 'Error'
        elif op=='lcm':
            value= math.lcm(n1,n2)
        elif op=='power':
            value= math.pow(n1,n2)
        else:
            value= "invalid op"
    # return value
    return render_template('index.html',value=value)
    

if __name__=='__main__':
    app.run(debug=True)