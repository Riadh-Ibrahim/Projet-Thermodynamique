import pandas as pd

# Charger les données expérimentales
data = pd.read_csv("data_calorimetrie.csv")

# Capacité thermique massique de l'eau
c_eau = 4185  # J/kg.K
m_eau = 0.25  # kg
C_calorimetre = 373  # J/K

# Calcul de la chaleur massique des solides
data["Q_perdu"] = (m_eau * c_eau + C_calorimetre) * (data["Tf_systeme (K)"] - data["Ti_eau (K)"])
data["Chaleur_massique_calculee"] = data["Q_perdu"] / (data["Masse_solide (kg)"] * (data["Tf_systeme (K)"] - data["Ti_solide (K)"]))

# Affichage des résultats
print(data)

# Comparaison avec les valeurs théoriques
print("Différence entre valeurs calculées et théoriques :")
print(data["Chaleur_massique"] - data["Chaleur_massique_calculee"])
