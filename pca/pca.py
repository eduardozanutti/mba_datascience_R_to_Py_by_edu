import numpy as np
import pandas as pd

def fatores_principais(df_std,df_scores,i):    
    fatores=[]
    array=[]
    bu=[]
    for n in range(len(df_std)):
            for m in range(len(df_scores)):
                fatores.append(sum(np.array(df_std.iloc[n,:])*np.array(df_scores.iloc[m,:])))   
            array.append([df_std.index[n]])
            bu.append(fatores)
            fatores=[]
    x=pd.DataFrame(array)
    y=pd.DataFrame(bu)
    lista_nomes=[]
    for nomes in range(i):
        lista_nomes.append(f'Fator {nomes+1}')
    saida=x.merge(y,left_index=True, right_index=True).iloc[:,1:].set_index(df_std.index)
    saida=saida.iloc[:,:i]
    saida.columns=lista_nomes
    return(saida)
