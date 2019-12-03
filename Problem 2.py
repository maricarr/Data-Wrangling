import pandas as pd
mess={'Box':['Box 1','Box 1','Box 1', 'Box 2','Box 2','Box 2'],'Dimension':['Length','Width','Height','Length','Width', 'Height'],'Value':[6,4,2,5,3,4]}
messy=pd.DataFrame(mess,columns=['Box','Dimension','Value'])
tformat=messy.pivot_table(index=['Box'],columns='Dimension',values='Value').reset_index()
volume=tformat['Volume']=tformat.Length*tformat.Height*tformat.Width
col=pd.DataFrame(tformat,columns=['Box','Height','Length','Width','Volume'])
