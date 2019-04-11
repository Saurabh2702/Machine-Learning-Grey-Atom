# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
new_record=np.array(new_record)
census=np.concatenate((new_record,data))


# --------------
#Code starts here
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here

con0=census[:,2]==0
race_0=census[con0]
len_0=len(race_0)

con1=census[:,2]==1
race_1=census[con1]
len_1=len(race_1)

con2=census[:,2]==2
race_2=census[con2]
len_2=len(race_2)

con3=census[:,2]==3
race_3=census[con3]
len_3=len(race_3)

con4=census[:,2]==4
race_4=census[con4]
len_4=len(race_4)

print(len_0,len_1,len_2,len_3,len_4)

minority_race=3





# --------------
#Code starts here
con0=census[:,0]>60
senior_citizens=census[con0]
working_hours_sum=senior_citizens[:,6].sum()
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
con1=census[:,1]>10
high=census[con1]

con2=census[:,1]<=10
low=census[con2]

avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()

if avg_pay_high>avg_pay_low:
  print('Higher Educated people have a better pay in general')
else:
  print("Pay doesn't depend on education")


