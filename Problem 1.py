import pandas as pd
math={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
maths=pd.DataFrame(math,columns=['Student','Math'])

elec={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
elecs=pd.DataFrame(elec,columns=['Student','Electronics'])

geas={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
geass=pd.DataFrame(geas,columns=['Student','GEAS'])


esat={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
esats=pd.DataFrame(esat,columns=['Student','ESAT'])


tidy=pd.merge(maths,elecs,how='left',on='Student')

tidy=pd.merge(tidy,geass,how='left',on='Student')

tidy=pd.merge(tidy,esats,how='left',on='Student')

melt= pd.melt (tidy, id_vars = 'Student', value_vars = ['Math','Electronics', 'GEAS', 'ESAT'])
long = melt.rename(columns = {'variable': 'Subject', 'value': 'Grades'})