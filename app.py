
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    <style>
        body {
            font-family: Arial;
            background: #eaf0f8;
            text-align: center;
            padding: 50px;
        }
        .box {
            background: white;
            padding: 30px;
            margin: auto;
            max-width: 350px;
            border-radius: 15px;
        }
        input, select, button {
            padding: 10px;
            margin: 10px;
            width: 85%;
        }
        button {
            background: blue;
            color: white;
            border: none;
            cursor: pointer;
        }
        h2 { color: blue; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Python Calculator</h2>

        <form method="POST">
            <input type="number" step="any"
                   name="a" placeholder="First number" required>

            <select name="op">
                <option value="+">Addition (+)</option>
                <option value="-">Subtraction (-)</option>
                <option value="*">Multiplication (*)</option>
                <option value="/">Division (/)</option>
            </select>

            <input type="number" step="any"
                   name="b" placeholder="Second number" required>

            <button type="submit">Calculate</button>
        </form>

        <h3>{{ result }}</h3>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = "Cannot divide by zero" if b == 0 else a / b

    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
