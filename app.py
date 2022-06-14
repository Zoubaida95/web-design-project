from flask import Flask, render_template, request

app = Flask(__name__)

database={"yara":"12345","zubaida":"2222"}

@app.route("/")
def home():
    return render_template("login.html")
@app.route("/login",methods=["POST"])
def login():
    name=request.form['username']
    password=request.form['password']
    if name in database:
        if database[name]==password:
            return render_template("homepage.html")
        else:
            return render_template("login.html", info="wrong password")
    else:
        return render_template("login.html", info="wrong password or username")
@app.route('/signup',methods=["POST","GET"])
def signup():
    if not request.form:
        return render_template("signup.html")
    database[request.form['username']]=request.form['password']
    return render_template("login.html")

@app.route("/home")
def homepage():
    return render_template("homepage.html")
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)