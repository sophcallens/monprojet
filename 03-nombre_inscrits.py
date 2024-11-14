import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = df.groupby('Libellé du département')['Inscrits'].sum()
print(pd.DataFrame(df1))
