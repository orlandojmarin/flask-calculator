from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add/<int:a>/<int:b>')
def addition(a, b):
    result = a + b
    return render_template("index.html", operation="Addition", result=result)

@app.route('/subtract/<int:a>/<int:b>')
def subtraction(a, b):
    result = a - b
    return render_template("index.html", operation="Subtraction", result=result)

@app.route('/multiply/<int:a>/<int:b>')
def multiplication(a, b):
    result = a * b
    return render_template("index.html", operation="Multiplication", result=result)

@app.route('/divide/<int:a>/<int:b>')
def division(a, b):
    if b == 0:
        return render_template("index.html", operation="Division", result="Error: Cannot divide by zero")
    result = a / b
    return render_template("index.html", operation="Division", result=result)

if __name__ == '__main__':
    app.run(debug=True)
