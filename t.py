import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.DataFrame(columns=["Nom", "pos", "neg"])
df = df.append({"Nom": "Provencece", "pos": 150, "neg": 25 }, ignore_index = True)
df = df.append({"Nom": "Tahiti", "pos": 54, "neg": 125 }, ignore_index = True)
df.plot(y= ["pos","neg"], x='Nom', kind='bar')
plt.show()

print(df)