from flask import Flask,render_template
app=Flask(__name__)

@app.route("/bio")
def info():
    return render_template('info.html')

app.run(debug=True)