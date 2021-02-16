import pandas as pd
from matplotlib.pyplot import scatter, savefig, figure, plot, clf

dataframe = pd.read_csv('resultados 1/Resultados_100 nodos.csv', index_col=0)

list_func = []
for index, row in dataframe.iterrows():
    if not (row.Funcion in list_func):
        list_func.append(row.Funcion)
        
print (list_func)
qa
for func in list_func:
    df_slice = dataframe [dataframe ['Funcion'] == func]
    df_slice = df_slice[['Mejor_Valor','Tiempo']]
    print("\n",func)
    print (df_slice.describe())
    func = func[1:-1]
    df_slice.describe().to_csv('resultados_'+func+'.csv')
    
    plot(df_slice['Mejor_Valor']]
    savefig (''

#print (dataframe['Funcion'])

#print (dataframe)
