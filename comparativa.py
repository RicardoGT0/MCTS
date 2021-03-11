from os import scandir, path
import pandas as pd
dic_funciones={}

def comparativa(ruta):
    for elemento in scandir(ruta):
        if path.isdir(elemento):
            comparativa(ruta+'/'+elemento.name)
        else:
            if elemento.name[-3:] == 'csv':
                elemento_div= elemento.name.split('\'')
                if len(elemento_div) > 2:
                    df_desc = pd.read_csv(ruta+'/'+elemento.name,index_col=0)
                    std = df_desc.at['std', 'Mejor_Valor']
                    mean = df_desc.at['mean', 'Mejor_Valor']
                    ruta_div = ruta.split('/')[1]
                    if elemento_div[1] in dic_funciones:
                        if 'std_val' in dic_funciones[elemento_div[1]]:
                            if std < dic_funciones[elemento_div[1]]['std_val']:
                                dic_funciones[elemento_div[1]] ['mean_val'] = std
                                dic_funciones[elemento_div[1]] ['mean_ruta'] = ruta_div
                        if 'mean_val' in dic_funciones[elemento_div[1]]:
                            if mean < dic_funciones[elemento_div[1]]['mean_val']:
                                dic_funciones[elemento_div[1]] ['mean_val'] = mean
                                dic_funciones[elemento_div[1]] ['mean_ruta'] = ruta_div
                    else:
                        dic_funciones[elemento_div[1]] = {'std_ruta': ruta_div, 'std_val': std, 'mean_ruta': ruta_div, 'mean_val': mean}

if __name__ == "__main__":
    ruta='resultados'
    comparativa(ruta)
    data = pd.DataFrame.from_dict(dic_funciones,orient='index')
    data.to_csv(ruta+'/comparativa.csv')
