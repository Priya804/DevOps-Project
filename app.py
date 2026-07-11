from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# Temporary in-memory employee database
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"}
]


@app.route("/")
def home():
    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        emp = {
            "id": len(employees) + 1,
            "name": request.form["name"],
            "department": request.form["department"]
        }

        employees.append(emp)

        return redirect("/")

    return render_template("add.html")


@app.route("/api/employees")
def api():

    return jsonify(employees)


@app.route("/health")
def health():

    return {
        "status": "UP"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)