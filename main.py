from flask import Flask, render_template
'''flask --app main --debug run'''
app = Flask(__name__)


nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "О спортивном программировании", "URL": "/aboutsp" },
    { "title": "Задания", "URL": "/tasks" },
    { "title": "Плюсы и минусы спортивного программирования", "URL": "/plusandminussp" },
    { "title": "Глоссарий", "URL": "/glossary" },
    { "title": "Обо мне", "URL": "/about" }
]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/")
def home():
    return render_template("home.html", name = "Главная")

@app.route("/aboutsp")
def aboutsp():
    return render_template("aboutsp.html", name = "О спортивном программировании")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html", name = "Задания")

@app.route("/plusandminussp")
def achievements():
    return render_template("plusandminussp.html", name = "Плюсы и минусы спортивного программирования")

@app.route("/glossary")
def glossary():
    return render_template("glossary.html", name = "Глоссарий")

@app.route("/about")
def about():
    return render_template("about.html", name = "Обо мне")

if __name__ == '__main__':
    app.run(debug=True)