import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1=df.groupby('Libellé du département').sum()

df2 = {}
for column in df1.columns :
    if column in {col for col in df1.loc[:,'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN']} :
        df2[column] = [((df1[column]/df1['Inscrits'])*100).round(2)]

df3=pd.DataFrame( df2[column].nlargest(10))

for column in df2.columns :
    df3[column] = df2[column].nlargest(10)
df3


