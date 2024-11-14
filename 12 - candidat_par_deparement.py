import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = df.groupby('Libellé du département').sum().loc[:,'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN']

df2=pd.DataFrame()
df2['candidat préféré'] = df1.idxmax(axis=1)

print(df2)
