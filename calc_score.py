import pandas as pd
from matplotlib.pyplot import plot, savefig, clf, legend, tight_layout
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
    #print (list_func)

    for func in list_func:
        df_slice = dataframe [dataframe ['Funcion'] == func]
        df_slice = df_slice[['Mejor_Valor','Tiempo']]
        #print("\n",func)
        #print (df_slice.describe())
        func = func[1:-1]
        df_desc = df_slice.describe()
        df_desc.to_csv(ruta+'/analisis/resultados_'+func+'.csv')

        std = df_desc.at['std', 'Mejor_Valor']
        mean = df_desc.at['mean', 'Mejor_Valor']
        stdmas = std + mean
        stdmenos = mean - std
        plot(range(0, 22), [mean] * 22, 'k--', label='media')
        plot(range(0, 22), [stdmas] * 22, 'r--', label='Media + Desviación Estándar')
        plot(range(0, 22), [stdmenos] * 22, 'g--', label= 'Media - Desviación Estándar')
        plot(range(1, 21), df_slice['Mejor_Valor'], label='Mejor valor por ronda')
        lg=legend(bbox_to_anchor=(1.0, 1.0), loc='upper left', shadow=True )

        savefig(ruta+'/analisis/' + func + '.png', format='png',bbox_extra_artists=(lg,), bbox_inches='tight')
        clf()


if __name__ == "__main__":
    calc_score()
