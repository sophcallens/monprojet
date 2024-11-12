import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

nom=input('De quelle candidats souhaitez vous connaitre le nombre de vote (inscrivez le Prenom NOM)')
somme = df[nom].sum()
print(somme)