import pandas as pd
from seaborn import lineplot
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
    grafico = lineplot(y='Mejor_Valor', data=df_slice).figure.savefig ("analisis/"+func+".png")
    

#print (dataframe['Funcion'])

#print (dataframe)
