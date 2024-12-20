import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")


df1={}
for column in df.columns : 
    if column not in {'Code du département','Libellé du département','Code de la circonscription','Inscrits','Votants','Exprimés'} : #suppression des collones qui ne nous interessent pas
        df1[column] = [((df[column].sum()/df['Inscrits'].sum())*100).round(2)] #calcul du pourcentage de vote par candidat

print(pd.DataFrame(df1))


