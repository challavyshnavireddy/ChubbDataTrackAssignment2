from flask import Flask,request,render_template

app=Flask(__name__)
history={}
@app.route("/",methods=['GET','POST'])
def feedback():
    global history
    if request.method == 'POST':
        name=request.form.get('name')
        feedback=request.form.get('feedback')
        if name and feedback:
            history[name]=feedback
    return render_template('feedbackform.html',history=history)

if __name__=="__main__":
    app.run(debug=True)