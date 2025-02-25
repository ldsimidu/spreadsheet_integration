import pandas as pd
caminho_excel = "spreadsheets/tests-ss.xlsx"

pf = pd.read_excel(caminho_excel)
print(pf)