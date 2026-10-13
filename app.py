from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kurs = request.form["kurs"]
        kommentar = request.form["kommentar"]
        return render_template("resultat.html", 
                               navn=navn,
                               epost=epost,
                               alder=alder,
                               kommentar=kommentar,
                               kurs=kurs
                               )
    return render_template("form.html")


    

if __name__ == "__main__":
    app.run(debug = True)