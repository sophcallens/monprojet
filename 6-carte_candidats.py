import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1=pd.DataFrame()
for column in df.columns:
    if column not in {'Code du département','Libellé du département','Code de la circonscription','Inscrits','Votants','Exprimés','Abstentions','Blancs','Nuls'}:
        df1[column] = ((df.groupby('Libellé du département')[column].sum() / df.groupby('Libellé du département')['Inscrits'].sum()) * 100).round(2)
df1



# +
departements = gpd.read_file('departements-version-simplifiee.geojson')
departements = departements.merge(df1, on='index')

departements.plot(column=df1.max(axis = departement), legend=True, edgecolor='black')
plt.title('Candidat le plus voté par département')
plt.axis('off')
plt.show()
# -






