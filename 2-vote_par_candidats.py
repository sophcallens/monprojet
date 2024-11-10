import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

<<<<<<< HEAD
df1=pd.DataFrame()
=======
df1={}
>>>>>>> d4a1cfa94625c5dda0c37c344b87ff8867ee65ed
for column in df.columns : 
    if column not in {'Code du département','Libellé du département','Code de la circonscription','Inscrits','Votants','Exprimés'} :
        df1[column] = [((df[column].sum()/df['Inscrits'].sum())*100).round(2)]

<<<<<<< HEAD
print(df1)
=======
print(pd.DataFrame(df1))
>>>>>>> d4a1cfa94625c5dda0c37c344b87ff8867ee65ed
