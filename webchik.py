from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('about_me.html', title="Про себе")

@app.route("/grad_page")
def studying():
    return render_template('graduation.html', title="освіта")

@app.route("/proj_page")
def works():
    return render_template('projects.html', title="проекти")

@app.route("/cont_page")
def feedback():
    return render_template('contacts.html', title="контакти")

















if __name__ == "__main__":
    app.run()

