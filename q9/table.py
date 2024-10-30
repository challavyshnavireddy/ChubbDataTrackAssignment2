from flask import Flask,render_template

app=Flask(__name__)

details=[{"name":"Hari",
           "age":21,
           "city":"Hyderabad"},
           {"name":"Priya",
           "age":25,
           "city":"Hyderabad"},
           {"name":"Mahi",
           "age":31,
           "city":"Banglore"},
           {"name":"Swathi",
           "age":32,
           "city":"Bhuvneshwar"},
           {"name":"Harika",
           "age":19,
           "city":"Chennai"},
           {"name":"Gopi",
           "age":21,
           "city":"Hyderabad"},
           {"name":"Gnashi",
           "age":27,
           "city":"Hyderabad"}]


@app.route('/')
def table():
    return render_template("table.html",details=details)

if __name__=='__main__':
    app.run(debug=True)
