# --------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
ax = gender_count.plot(kind='bar',figsize=(15,10))


# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(alignment,explode=(0.05,0.05,0.05))
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df=data[['Strength','Combat']].copy()

#covariance=sc_df.Strength.cov(sc_df.Combat)
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)

ic_df=data[['Intelligence','Combat']].copy()
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=ic_df.Intelligence.std()
ic_combat=ic_df.Combat.std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=data[data['Total']>=total_high].copy()
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

ax_1=plt.subplot(3, 1, 1)
ax_2=plt.subplot(3, 1, 2)
ax_3=plt.subplot(3, 1, 3)

ax_1.boxplot(super_best.Intelligence)
ax_1.set_title('Intelligence')

ax_2.boxplot(super_best.Speed)
ax_2.set_title('Speed')

ax_3.boxplot(super_best.Power)
ax_3.set_title('Power')



