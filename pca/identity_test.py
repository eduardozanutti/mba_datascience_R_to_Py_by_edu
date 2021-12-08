
import numpy as np
import math
from scipy.stats import chi2
from scipy import stats

def chi2_barlett_test(rho,n):
    #rho -> Matriz de correlação de Pearson mxm (mesma dimensão)
    #n -> Tamanho amostral
    if rho.shape[0]!= rho.shape[1]:
        print("Matriz de dimensões diferentes, insira uma matriz rho correta")
    else:
        k=rho.shape[1] #Quantidade de variáveis
        D=np.linalg.det(rho) #Determinante de rho
        df=(k*(k-1))/2 #Graus de Liberdade
        chi2_barlett=-math.log(D)*(n-1-(2*k+5)/6) #Chi2_Barlett
        p_value = 1-stats.chi2.cdf(x=chi2_barlett,df=df) #p_value para o Chi2_Barlett
        print('|---------------------TESTE DE ESFERICIDADE DE BARTLETT--------------------------------|')
        print()
        print('  Chi2 de Barllet = ',chi2_barlett)
        if p_value <0.05:
            print('  p-value = ',p_value,'***')
        else: print('  p-value = ',p_value)
        print('  Graus de Liberdade = ',int(df))
        print()
        if p_value <0.05:
            print('  RESULTADO = H1: A matriz rho NÃO é estatisticamente igual a uma matriz Identidade')
        else: 
            print('  RESULTADO = H0: A matriz rho É estatisticamente igual a uma matriz Identidade')
        print('|--------------------------------------------------------------------------------------|')
