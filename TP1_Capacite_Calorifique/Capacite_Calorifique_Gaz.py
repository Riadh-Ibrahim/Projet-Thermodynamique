import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("data_Cv_Cp.csv")

# Constantes
R = 8.314  # Constante des gaz parfaits J/(mol.K)
n = 1  # 1 mole d'air
P = 101325  # Pression atmosphérique en Pa
V = 0.0224  # Volume molaire en m^3 à CNTP

# Calcul de Cv à partir de la pente de Delta_P = f(T)
data["Cv"] = (P * V / (n * R)) * ((data["Tension (V)"] * data["Intensité (A)"]) / (data["Delta_P (Pa)"]))

# Affichage des résultats
print(data)

# Tracé de Cv en fonction de la température
plt.plot(data["Temperature (K)"], data["Cv"], marker='o', linestyle='-')
plt.xlabel("Température (K)")
plt.ylabel("Capacité Calorifique Cv (J/mol.K)")
plt.title("Évolution de Cv en fonction de la température")
plt.grid()
plt.show()