import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

somme = df['Inscrits'].sum()
print(somme)