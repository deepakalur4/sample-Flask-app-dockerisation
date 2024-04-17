from flask import Flask,render_template,request


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("predict_page.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
        return request.form["marks 1"] + request.form["marks 2"]
    else:
        return "No respose"
    

if __name__=="__main__":
    app.run(debug=True)