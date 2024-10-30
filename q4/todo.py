from flask import Flask,request,render_template,url_for,redirect

app=Flask(__name__)
l=[]

@app.route('/')
def show():
    return render_template('show.html',l=l)

@app.route('/create',methods=['GET','POST'])
def todoList():
    if request.method=='POST':
        task=request.form['task']
        if task:
            l.append(task)
        return redirect(url_for('show'))
    return render_template('create.html',l=l)
if __name__=='__main__':
    app.run(debug=True)