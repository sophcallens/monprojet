import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1=pd.DataFrame()
for column in df.columns:
    if column not in {'Code du département', 'Libellé du département', 'Code de la circonscription', 'Inscrits', 'Votants', 'Exprimés', 'Abstentions', 'Blancs', 'Nuls'} :
        df1[column] = ((df.groupby('Libellé du département')[column].sum() / df.groupby('Libellé du département')['Inscrits'].sum()) * 100).round(2)

print(df1)




