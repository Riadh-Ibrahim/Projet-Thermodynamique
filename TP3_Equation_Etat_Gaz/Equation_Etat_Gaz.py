import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("data_lois_gaz.csv")

# Loi de Boyle-Mariotte : PV = cste
plt.figure(figsize=(8,5))
plt.plot(1 / data["Volume (cm3)"], data["Pression (Pa)"], 'o-', label="Boyle-Mariotte (P = f(1/V))")
plt.xlabel("1/Volume (cm³)")
plt.ylabel("Pression (Pa)")
plt.legend()
plt.grid()

# Loi de Charles : P/T = cste
plt.figure(figsize=(8,5))
plt.plot(data["Temperature (K)"], data["Pression (Pa)"], 'o-', label="Charles (P = f(T))")
plt.xlabel("Température (K)")
plt.ylabel("Pression (Pa)")
plt.legend()
plt.grid()

# Loi de Gay-Lussac : V/T = cste
plt.figure(figsize=(8,5))
plt.plot(data["Temperature (K)"], data["Volume (cm3)"], 'o-', label="Gay-Lussac (V = f(T))")
plt.xlabel("Température (K)")
plt.ylabel("Volume (cm³)")
plt.legend()
plt.grid()

plt.show()
