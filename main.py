import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

caminho_excel = "spreadsheets/tests-ss.xlsx"

pf = pd.read_excel(caminho_excel)
#print(pf)

@app.route("/")
def show_table():
    pf = pd.read_excel(caminho_excel)
    full_table = pf.to_html(classes="table table-striped")
    total_table = pf[["Times","TOTAL"]].to_html(classes="table table-stripped")
    
    return render_template("index.html", tabela=total_table)

if __name__ == "__main__":
    app.run(debug=True)