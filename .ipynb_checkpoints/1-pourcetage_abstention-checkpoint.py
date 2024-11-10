import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")



df1 = df.groupby('Libellé du département')[['Inscrits','Abstentions']].sum()

df1['Pourcentage d\'abstentions']= ((df1['Abstentions']/df1['Inscrits'])*100).round(2)

df2 = df1[['Pourcentage d\'abstentions']]
df2.head()


