import pandas as pd
from seaborn import lineplot
from os import mkdir

def calc_score():
    f = open('last_path.txt', 'r')
    ruta = f.read()
    f.close()
    try:
        mkdir(ruta+'/analisis')
    except:
        print("El directorio ", ruta, " ya existe")

    dataframe = pd.read_csv(ruta+'/Resultados.csv', index_col=0)

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
        df_desc.to_csv(ruta+'/analisis/resultados_'+func+'.csv')
        grafico=lineplot(data=df_slice['Mejor_Valor'])
        grafico.figure.savefig (ruta+'/analisis/'+func+'.png')
        grafico.figure.clf()


    #print (dataframe['Funcion'])

    #print (dataframe)

calc_score()