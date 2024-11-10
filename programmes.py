import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

def f1(df):
    df1 = df.groupby('Libellé du département')[['Inscrits','Abstentions']].sum()
    df1['Pourcentage d\'abstentions']= ((df1['Abstentions']/df1['Inscrits'])*100).round(2)
    return df1[['Pourcentage d\'abstentions']]

def f2(df):
    df1=pd.DataFrame()
    for column in df.columns : 
        if column not in {'Code du département','Libellé du département','Code de la circonscription','Inscrits','Votants','Exprimés'} :
            df1[column] = [((df[column].sum()/df['Inscrits'].sum())*100).round(2)]
    return df1

def f3(df) :
    df1 = df.groupby('Libellé du département')['Inscrits'].sum()
    return df1

def f4(df) :
    df1=df.groupby('Libellé du département').sum()

    df2 = {}
    for column in df1.columns :
        if column in {col for col in df1.loc[:,'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN']} :
            df2[column] = [((df1[column]/df1['Inscrits'])*100).round(2)]

    df3=pd.DataFrame( df2[column].nlargest(10))

    for column in df2.columns :
        df3[column] = df2[column].nlargest(10)
    return df3

