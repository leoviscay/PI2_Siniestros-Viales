import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

########################################## FUNCIONES ##############################################


######################### INFORMACION O MODIFICACION COLUMNAS #####################################

def types_data_df(df):
    '''
    Analiza de los tipos de datos en un DataFrame y devuelve un resumen que incluye información sobre
    los tipos de datos en cada columna, el porcentaje de valores no nulos y nulos, así como la
    cantidad de valores nulos por columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre_campo': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
        - 'no_nulos_%': Porcentaje de valores no nulos en cada columna.
        - 'nulos_%': Porcentaje de valores nulos en cada columna.
        - 'nulos': Cantidad de valores nulos en cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": [], "nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict["nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def convert_to_datatime(x):
    '''
    Convierte un valor a un objeto de tiempo (time) de Python si es posible.

    Esta función acepta diferentes tipos de entrada y trata de convertirlos en objetos de tiempo (time) de Python.
    Si la conversión no es posible, devuelve None.

    Parameters:
        x (str, datetime, or any): El valor que se desea convertir a un objeto de tiempo (time).

    Returns:
        datetime.time or None: Un objeto de tiempo (time) de Python si la conversión es exitosa,
        o None si no es posible realizar la conversión.
    '''
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x




######################################## GRAFICAS #########################################




def accidentes_x_mes_x_año(df):
    '''
    Crea gráficos de líneas para la cantidad de víctimas de accidentes mensuales por año.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes, con una columna 'Año'.

    Returns:
        None
    '''
    # Se obtiene una lista de años únicos
    años = df['Año'].unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se definen colores personalizados
    colores = plt.cm.viridis(np.linspace(0, 1, len(años)))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        # Se filtran los datos para el año actual y agrupa por mes
        data_mensual = (df[df['Año'] == year]
                        .groupby('Mes')
                        .agg({'Cantidad víctimas':'sum'}))
        
        # Se configura el subgráfico actual
        ax = axes[fila, columna]
        ax.plot(data_mensual.index, data_mensual['Cantidad víctimas'], color=colores[i], label=f'Año {year}')
        ax.set_xlabel('Mes')
        ax.set_ylabel('Cantidad de Víctimas')
        ax.legend(loc='upper right')  # Muestra la leyenda en la esquina superior derecha
        
    # Se muestra y acomoda el gráfico
    plt.tight_layout()
    plt.show()



def victimas_x_mes_total_años(df):
    '''
    Crea un gráfico de líneas que muestra la cantidad total de víctimas de accidentes por mes a lo largo de los años.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Mes' y 'Cantidad víctimas'.

    Returns:
        None
    '''
     # Se agrupa por la cantidad de víctimas por mes
    data = df.groupby('Mes').agg({'Cantidad víctimas':'sum'}).reset_index()
    
    # Se obtienen los colores del mapa de colores viridis
    colores = sns.color_palette("viridis", n_colors=len(data['Mes']))
    
    # Se grafica
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(x='Mes', y='Cantidad víctimas', data=data, color=colores[0], marker='o')
    ax.set_title('Cantidad total de víctimas por Mes a lo largo de los años')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Cantidad de Víctimas')
    
    # Modificar etiquetas del eje x para mostrar los meses
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ax.set_xticks(data['Mes'])
    ax.set_xticklabels(meses)
    
    # Se añaden etiquetas en los picos de las líneas
    for i, txt in enumerate(data['Cantidad víctimas']):
        ax.annotate(txt, (data['Mes'][i], data['Cantidad víctimas'][i]),
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    # Se muestra el gráfico
    plt.show()


def victimas_x_dia_semana_años(df):
    '''
    Crea un gráfico de líneas que muestra la cantidad de víctimas de accidentes por día de la semana.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Fecha'.

    Returns:
        None
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Día semana'] = df['Fecha'].dt.dayofweek
    
    # Se mapea el número del día de la semana a su nombre
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    df['Nombre día'] = df['Día semana'].map(lambda x: dias_semana[x])
    
    # Se establece el orden de los días de la semana
    df['Nombre día'] = pd.Categorical(df['Nombre día'], categories=dias_semana, ordered=True)
    
    # Se cuenta la cantidad de accidentes por día de la semana
    data = df.groupby('Nombre día').agg({'Cantidad víctimas':'sum'}).reset_index()
    
    # Se obtienen los colores del mapa de colores viridis
    colores = sns.color_palette("viridis", n_colors=len(data['Nombre día']))
    
    # Se grafica
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(x='Nombre día', y='Cantidad víctimas', data=data, sort=False, color=colores[0], marker='o')
    ax.set_title('Cantidad de Víctimas de Accidentes por Día de la Semana')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Cantidad de Víctimas')
    
    # Se añaden etiquetas en los picos de las líneas
    for i, txt in enumerate(data['Cantidad víctimas']):
        ax.annotate(txt, (data['Nombre día'][i], data['Cantidad víctimas'][i]),
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    # Se muestra el gráfico
    plt.show()

def accidentes_x_hora_diario(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por hora del día.

    Parameters:
        df (pandas.DataFrame): El conjunto de datos de accidentes con una columna 'Hora'.

    Returns:
        Un gráfico de barras.
    '''
    # Se extrae la hora del día de la columna 'Hora'
    df['Hora del día'] = df['Hora'].apply(lambda x: x.hour)

    # Se cuenta la cantidad de accidentes por hora del día
    data = df['Hora del día'].value_counts().reset_index()
    data.columns = ['Hora del día', 'Cantidad de accidentes']

    # Se ordena los datos por hora del día
    data = data.sort_values(by='Hora del día')

    # Se obtienen los colores del mapa de colores viridis
    colores = sns.color_palette("viridis", n_colors=len(data['Hora del día']))
    
    # Se grafica
    plt.figure(figsize=(12, 4))
    ax = sns.barplot(x='Hora del día', y='Cantidad de accidentes', data=data, palette=colores)

    ax.set_title('Cantidad de Accidentes por Hora del Día') 
    ax.set_xlabel('Hora del día')
    ax.set_ylabel('Cantidad de accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (row["Hora del día"], row["Cantidad de accidentes"]), ha='center', va='bottom')

    # Se muestra el gráfico
    plt.show()


def cantidad_victimas_sexo_rol_victima(df):
    '''
    Genera un resumen de la cantidad de víctimas por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de víctimas por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de víctimas por sexo, rol y tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Gráfico 1: Sexo
    sns.countplot(data=df, x='Sexo', ax=axes[0])
    axes[0].set_title('Cantidad de víctimas por sexo') ; axes[0].set_ylabel('Cantidad de víctimas')

    # Se define una paleta de colores personalizada (invierte los colores)
    colores_por_defecto = sns.color_palette()
    colores_invertidos = [colores_por_defecto[1], colores_por_defecto[0]]
    
    # Gráfico 2: Rol
    df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)
    df_rol.plot(kind='bar', stacked=True, ax=axes[1], color=colores_invertidos)
    axes[1].set_title('Cantidad de víctimas por rol') ; axes[1].set_ylabel('Cantidad de víctimas') ; axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)
    
    # Gráfico 3: Tipo de vehículo
    df_victima = df.groupby(['Víctima', 'Sexo']).size().unstack(fill_value=0)
    df_victima.plot(kind='bar', stacked=True, ax=axes[2], color=colores_invertidos)
    axes[2].set_title('Cantidad de víctimas por tipo de vehículo') ; axes[2].set_ylabel('Cantidad de víctimas') ; axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    # Se muestran los gráficos
    plt.show()

def cantidad_victimas_participantes(df):
    '''
    Genera un resumen de la cantidad de víctimas por número de participantes en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por número de participantes en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por número de participantes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['Participantes'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'participantes'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    # Se crea el gráfico de barras
    ax = sns.barplot(data=ordenado, x='Participantes', y='count', order=ordenado['Participantes'])
    ax.set_title('Cantidad de víctimas por participantes')
    ax.set_ylabel('Cantidad de víctimas')
    # Rotar las etiquetas del eje x a 45 grados
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()



   