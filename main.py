import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

caminho_excel = "spreadsheets/tests-ss.xlsx"

pf = pd.read_excel(caminho_excel)
#print(pf)

@app.route("/")
def show_table():
    pf = pd.read_excel(caminho_excel)
    tabela_html = pf.to_html(classes="table table-striped")
    
    return render_template("index.html", tabela=tabela_html)

if __name__ == "__main__":
    app.run(debug=True)