import pandas as pd
from matplotlib.pyplot import scatter, savefig, figure, plot, clf, show, legend
from os import system

dataframe = pd.read_csv('resultados/Resultados_100 nodos.csv', index_col=0)

list_func = []
for index, row in dataframe.iterrows():
    if not (row.Funcion in list_func):
        list_func.append(row.Funcion)
        
print (list_func)

for func in list_func:
    df_slice = dataframe [dataframe ['Funcion'] == func]
    df_slice = df_slice[['Mejor_Valor','Tiempo']]
    print("\n",func)
    print (df_slice.describe())
    func = func[1:-1]
    df_desc = df_slice.describe()
    df_desc.to_csv('analisis/resultados_'+func+'.csv')
    std = df_desc.at['std', 'Mejor_Valor']
    mean = df_desc.at['mean', 'Mejor_Valor']
    stdmas = std + mean
    stdmenos = mean-std
    plot(range(0,22), [mean]*22, 'k--', label='media')
    plot(range(0,22), [stdmas]*22, 'r--')
    plot(range(0,22), [stdmenos]*22, 'g--')
    plot(range(1,21), df_slice['Mejor_Valor'])
    leyendas = ('Media', 'Media + Desviación Estándar', 'Media - Desviación Estándar', 'Mejor valor por ronda')
    legend(leyendas, loc='upper center', shadow=True, )
    savefig ("analisis/"+func+".png", format="png")
    clf()

#print (dataframe['Funcion'])

#print (dataframe)
