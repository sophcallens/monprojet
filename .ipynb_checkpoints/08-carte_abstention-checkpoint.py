# +
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = df.groupby('Libellé du département')[['Inscrits','Abstentions']].sum()
df2 = pd.DataFrame()
df2['Pourcentage d\'abstentions']= ((df1['Abstentions']/df1['Inscrits'])*100).round(2)
# fait par la fonction f1

departements = gpd.read_file('departements-version-simplifiee.geojson')
df3 = departements.merge(df2, left_on='nom', right_index=True, how='left')

df3.plot(column='Pourcentage d\'abstentions', legend=True, edgecolor=None, cmap='coolwarm', vmin=0, vmax=50)
plt.title('Pourcentage d\'abstentions par département')
plt.axis('off')
plt.show()



