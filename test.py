import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


departements = gpd.read_file('departements-version-simplifiee.geojson')


# Tracer une carte avec des couleurs différentes par département
departements.plot(column='nom', cmap='tab20', edgecolor='black', legend=False)
plt.title('Carte des Départements Français')
plt.axis('off')  # Supprime les axes pour une meilleure lisibilité
plt.show()


data = {'nom': ['Paris', 'Gironde', 'Rhône', 'Nord', 'Bouches-du-Rhône'],
        'population': [2200000, 1600000, 1800000, 2600000, 2000000]}

df = pd.DataFrame(data)

# Joindre les données à la carte
departements = departements.merge(df, on='nom')

# Tracer la carte selon la population
departements.plot(column='population', cmap='OrRd', legend=True, edgecolor='black')
plt.title('Population par Département')
plt.axis('off')
plt.show()