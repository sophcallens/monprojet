import pandas as pd

#récuperation données

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

#calcul somme

somme = df['Inscrits'].sum()
print(somme)