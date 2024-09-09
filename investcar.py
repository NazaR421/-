import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('carbase.csv')
#df.index = [df["Name"][0],df["Name"][3],df["Name"][6]]
df['Sales'].plot(kind = 'barh', color="violet")
plt.xlabel('Дні тижня')
plt.title('Середньодобова температура за тиждень')
plt.show()
