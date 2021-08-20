from flask  import Flask, render_template, url_for, request

app = Flask(__name__)

# route to homepage
@app.route("/")
def index():
    return render_template("index.html")

# route to about page
@app.route("/about")
def about():
    return render_template("about.html")

# route to password generator page
@app.route("/passwords")
def pass_gen():
    return render_template("pass_generator.html")

# Password generator Form Submission Rout

if __name__ == "__main__":
    app.run(debug=True)