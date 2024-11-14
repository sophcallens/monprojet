import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def f1(df):
    df1 = df.groupby('Libellé du département')[['Inscrits','Abstentions']].sum()
    df2 = pd.DataFrame()
    df2['Pourcentage d\'abstentions']= ((df1['Abstentions']/df1['Inscrits'])*100).round(2)
    return (df2)

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

def f5(df) :
    from région import REGIONS
    
    def attribuer_region(code):
        for region in REGIONS:
            for code_dep in REGIONS[region]:
                if str(code) == code_dep:
                    return region
        return 'Étranger'
    
    df['Région'] = df['Code du département'].apply(attribuer_region)
    
    df1 = df.groupby('Région').sum().loc[:,'Inscrits':'Nicolas DUPONT-AIGNAN']
    
    df2=pd.DataFrame()
    for column in df1.columns:
        if column not in {'Inscrits', 'Votants', 'Exprimés'}:
            df2[column] = ((df1[column] / df1['Inscrits']) * 100).round(2)
    return df2


def f6(df) :    
    df2 = f12(df)
    
    departements = departements.merge(df2, left_on='nom', right_index=True, how='left')
    
    departements.plot(column='candidat', legend=True, edgecolor='black', cmap='tab20')
    plt.title('Candidat préféré par département')
    plt.axis('off')
    plt.show()

def f7(df) :
    df1 = f3(df)
    
    departements = gpd.read_file('departements-version-simplifiee.geojson')
    df2 = departements.merge(df1, left_on='nom', right_index=True, how='left')
    
    df2.plot(column='Inscrits', legend=True, edgecolor='black', cmap='Reds')
    plt.title("Nombre d'inscrits par département")
    plt.axis('off')
    plt.show()

def f8(df) :
    df2 = f1(df)
    
    departements = gpd.read_file('departements-version-simplifiee.geojson')
    df3 = departements.merge(df2, left_on='nom', right_index=True, how='left')
    
    df3.plot(column='Pourcentage d\'abstentions', legend=True, edgecolor=None, cmap='coolwarm', vmin=0, vmax=50)
    plt.title('Pourcentage d\'abstentions par département')
    plt.axis('off')
    plt.show()

def f9(df) :
    somme = df['Inscrits'].sum()
    return (somme)

def f10(df) :
    nom=input('De quelle candidats souhaitez vous connaitre le nombre de vote (inscrivez le Prenom NOM) : ')
    somme = df[nom].sum()
    return 'Le résultat pour '+ nom + ' est '+ str(somme)

def f11(df) :
    df1=pd.DataFrame()
    for column in df.columns:
        if column not in {'Code du département', 'Libellé du département', 'Code de la circonscription', 'Inscrits', 'Votants', 'Exprimés', 'Abstentions', 'Blancs', 'Nuls'} :
            df1[column] = ((df.groupby('Libellé du département')[column].sum() / df.groupby('Libellé du département')['Inscrits'].sum()) * 100).round(2)
    return df1

def f12(df) :
    df1 = df.groupby('Libellé du département').sum().loc[:,'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN']
    df2=pd.DataFrame()
    df2['candidat préféré'] = df1.idxmax(axis=1)
    return df2


df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

