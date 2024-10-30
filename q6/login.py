from flask import Flask,request,url_for,redirect,render_template,flash

app=Flask(__name__)
app.secret_key='abcde'

vusername="user"
vpassword="password"

@app.route('/')
def show():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')
        if name and password:
            if name==vusername and password==vpassword:
                return "<center><h1>Login Successful! Welcome {}<h1/><center/>".format(name)
            else:
                flash("Invalid username or password")
                return redirect(url_for('show'))
        else:
            flash("Enter both username and password")
            return redirect(url_for('show'))
    return redirect(url_for('show'))
if __name__=="__main__":
    app.run(debug=True)