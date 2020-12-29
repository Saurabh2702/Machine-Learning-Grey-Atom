# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
total=len(df)
fsum=0
for i in range(0,len(df)):
  if df.get_value(i,'fico')>700:
    fsum=fsum+1
p_a=fsum/total
print(p_a)
psum=0
for i in range(0,len(df)):
  if df.get_value(i,'purpose')=='debt_consolidation':
    psum=psum+1
p_b=psum/total
print(p_b)
df1=df[df['purpose']=='debt_consolidation'].copy()
isum=0
for i in range(0,len(df)):
  if df.get_value(i,'fico')>700 :
    if df.get_value(i,'purpose')=='debt_consolidation':
      isum=isum+1
p_a_b=isum/total
print(p_a_b)
result=True if p_a_b==p_a else False
print(result)
# code ends here


# --------------
# code starts here
total=len(df)
prob_lp=len(df[df['paid.back.loan']=='Yes'])/total
print(prob_lp)

prob_cs=len(df[df['credit.policy']=='Yes'])/total
print(prob_cs)

new_df=df[df['paid.back.loan']=='Yes']
isum=0
for i in range(0,len(df)):
  if df.get_value(i,'credit.policy')=='Yes':
      if df.get_value(i,'paid.back.loan')=='Yes' :
        isum=isum+1
prob_pd_cs=isum/len(new_df)
print(prob_pd_cs)

bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
purp_count=df.purpose.value_counts()
plt.bar(purp_count.index,purp_count)
df1=df[df['paid.back.loan']=='No']
purp_count_new=df1.purpose.value_counts()
plt.bar(purp_count_new.index,purp_count_new)
# code ends here


# --------------
# code starts here
inst_median=df.installment.median()
inst_mean=df.installment.mean()

df['installment'].hist(bins=50)
plt.plot([inst_median]*600, range(600), label='median')
plt.plot([inst_mean]*600, range(600), label='mean')
plt.show()

df['log.annual.inc'].hist(bins=50)
plt.show()

# code ends here


