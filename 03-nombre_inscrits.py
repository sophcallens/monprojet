import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = df.groupby('Libellé du département')['Inscrits'].sum() #calcul du nbr total d'inscrits groupé par département
print(pd.DataFrame(df1))
