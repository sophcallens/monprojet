import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = df.groupby('Libellé du département').sum().loc[:,'Nathalie ARTHAUD':'Nicolas DUPONT-AIGNAN']

df2=pd.DataFrame()
df2['candidat'] = df1.idxmax(axis=1)
#ceci peut etre appelé par la fonction f12


departements = gpd.read_file('departements-version-simplifiee.geojson')
df3 = departements.merge(df2, left_on='nom', right_index=True, how='left')

df3.plot(column='candidat', legend=True, edgecolor='black', cmap='tab20')
plt.title('Candidat préféré par département')
plt.axis('off')
plt.show()



