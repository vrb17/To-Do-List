from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder="templates")

todo_list = [{"task": "Sample", "completed": False}]

@app.route("/")
def index():
    return render_template("index.html", todo_list = todo_list)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todo_list.append({"task": todo, "completed": False})
    return redirect(url_for("index"))


@app.route("/alter/<int:index>", methods=["GET", "POST"])
def alter(index):
    todo = todo_list[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("alter.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todo_list[index]['completed'] = not todo_list[index]['completed']
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todo_list[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
