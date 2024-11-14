import pandas as pd
df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

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

print(df2)
