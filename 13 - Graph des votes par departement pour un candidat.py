import matplotlib.pyplot as plt
import pandas as pd

# Récuperation des données 

df = pd.read_excel("resultats-par-niveau-cirlg-t1-france-entiere.xlsx")
nom=input('De quel candidat souhaitez vous connaitre le graph')

x=df['Code du département'].tolist()
y=df[nom].tolist()

# Tracer le graphique
plt.plot(x, y, marker='o', linestyle='-')  
plt.xlabel("Axe X") 
plt.ylabel("Axe Y")  
plt.title("Graphique de Y en fonction de X") 
plt.grid(True) 
plt.show()  

          