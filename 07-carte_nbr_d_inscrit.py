import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")

df1 = pd.DataFrame(df.groupby('Libellé du département')['Inscrits'].sum())
# peut etre appelé par la fonction f3

departements = gpd.read_file('departements-version-simplifiee.geojson')
df2 = departements.merge(df1, left_on='nom', right_index=True, how='left')

df2.plot(column='Inscrits', legend=True, edgecolor='Gray', cmap='Reds')
plt.title("Nombre d'inscrits par département")
plt.axis('off')
plt.show()



