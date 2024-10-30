from flask import Flask,render_template
import random
app=Flask(__name__)
l = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "Dream big and dare to fail.",
    "The only way to do great work is to love what you do.",
    "It always seems impossible until it’s done."
]

@app.route('/',methods=['GET'])
def generateQuotes():
    value=random.choice(l)
    return render_template('generate.html',value=value)

if __name__=='__main__':
    app.run(debug=True)