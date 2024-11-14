import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

#création d'un tableau pour faciliter le calcul du pourcentage
df1 = df.groupby('Libellé du département')[['Inscrits','Abstentions']].sum()

#création du DataFrame avec en indice le Libellé du département et en oridnée le poucentage d'abstention
df2 = pd.DataFrame()
df2['Pourcentage d\'abstentions']= ((df1['Abstentions']/df1['Inscrits'])*100).round(2)


print(df2)


