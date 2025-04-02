from flask import Flask,request, render_template #pomocí toho rendrujeme html z templates

app = Flask(__name__)

@app.route("/")
def helloword():
    return render_template("index.html")
@app.route("/registrace", methods=["GET"])
def registrace():
        name = request.args.get("jmeno")
        cecka = request.args.get("pocet_cecek")
       
        if cecka != "" and cecka != None:
            if int(cecka) > 17:
                return render_template("registrace.html", jinja_name = name)
        return render_template("registrace.html")
            
if __name__ == "__main__": # zapínání aplikace 
    app.run(debug=True)