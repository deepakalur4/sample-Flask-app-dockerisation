from flask import Flask,render_template,request


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])
def predict_pipeline():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)