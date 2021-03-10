from flask import Flask, render_template, request
from products import Products

app = Flask(__name__)
db = Products()

@app.route("/")
def products():
    return render_template("products.html", products=db.products)

@app.route("/search", methods=["GET", "POST"])
def search():
    
    if request.method == "GET":
        return render_template("form.html")
    
    elif request.method == "POST":

        hasresults = False
        output = []

        if request.form["name"] != "":
            output = db.findbyName(request.form["name"])
        elif request.form["price"] != "":
            output = db.findbyPrice(request.form["price"])
        elif request.form["qty"] != "":
            output = db.findbyQty(request.form["qty"])

        if len(output) > 0:
            hasresults = True
        else:
            output = "No results found, sorry :("
        
        return render_template("form.html", hasresults=hasresults, output=output)


if __name__ == "__main__":
    app.run()
