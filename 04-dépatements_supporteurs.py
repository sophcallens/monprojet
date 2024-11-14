import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

#calcul du pourcentage de vote pour un candidat par département
df1=df.groupby('Libellé du département').sum() 

df2 = pd.DataFrame()
for column in df1.loc[:, 'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN'].columns:
    df2[column] = ((df1[column] / df1['Inscrits']) * 100).round(2)

#on assigne a chaque candidat les 10 départements qui ont le plus voté pour eux
df3 = pd.DataFrame()
for column in df2.columns :
    df3[column] = df2[column].nlargest(10).index
    
print(df3)



