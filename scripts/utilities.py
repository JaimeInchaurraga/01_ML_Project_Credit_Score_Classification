import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import f_oneway

def data_report(df):
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)


    return concatenado.T


# MODIFICADA PARA USAR DESPUÉS DE SPLIT DE DATOS
from scipy.stats import f_oneway
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_features_num_classification_dos(X, y, pvalue=0.05):
    """
    Identifica las columnas numéricas en X y las compara con la variable objetivo y
    para ver si existe correlación utilizando ANOVA.
    """
    if not isinstance(X, pd.DataFrame) or not isinstance(y, pd.Series):
        print("X debe ser un DataFrame y y debe ser una Serie de pandas.")
        return []
    
    if X.shape[0] != y.shape[0]:
        print("X e y deben tener el mismo número de filas.")
        return []
    
    num_cols = X.select_dtypes(include=np.number).columns.tolist()
    significant_cols = []
    
    for col in num_cols:
        f_value, p_value = f_oneway(*(X.loc[y == unique_value, col].dropna() for unique_value in y.unique()))
        if p_value <= pvalue:
            significant_cols.append(col)
    
    return significant_cols

def plot_features_num_classification_dos(X, y, columns=[], pvalue=0.05):
    """
    Genera pairplots para las columnas numéricas significativas basándose en ANOVA con la variable objetivo y.
    """
    significant_cols = get_features_num_classification_dos(X, y, pvalue)
    
    if columns:
        columns_to_plot = [col for col in columns if col in significant_cols]
    else:
        columns_to_plot = significant_cols
    
    if not columns_to_plot:
        print("No hay columnas significativas para pintar.")
        return
    
    temp_df = X.copy()
    temp_df['target'] = y
    
    sns.pairplot(temp_df, vars=columns_to_plot, hue='target')
    plt.show()



# FUNCION 2 JAIME
def get_features_num_classification(dataframe, target_col, pvalue=0.05):
    """
    Identifica las columnas numéricas en un DataFrame y las compara con una columna target de clasificación 
    para ver si existe correlación utilizando ANOVA, excluyendo aquellas columnas numéricas que son en realidad categóricas.
    
    Argumentos:
    dataframe (pd.DataFrame): El DataFrame que contiene los datos.
    target_col (str): Nombre de la columna objetivo que se considerará categórica si tiene baja cardinalidad o es del tipo categórico.
    pvalue (float): Umbral de valor p para la significancia estadística, 0.05 por defecto.

    Retorna:
    list: Lista de columnas numéricas que pasan la prueba de ANOVA.
    """

    # Comprobación de valores de entrada
    if not isinstance(dataframe, pd.DataFrame):
        print("El argumento 'dataframe' debe ser un DataFrame de pandas.")
        return None
    if not isinstance(target_col, str):
        print("El argumento 'target_col' debe ser una cadena de texto.")
        return None
    if not isinstance(pvalue, float):
        print("El argumento 'pvalue' debe ser un valor de punto flotante.")
        return None
    
    # Verificación de la existencia de la columna objetivo
    if target_col not in dataframe.columns:
        print(f"La columna '{target_col}' no se encuentra en el dataframe.")
        return None
    
    # Comprobación de la cardinalidad de la columna objetivo para determinar si puede ser tratada como categórica
    cardinalidad = len(dataframe[target_col].unique())
    if cardinalidad > 10:
        print(f"La columna '{target_col}' tiene alta cardinalidad, no puede ser Categórica.")
        return None
    
    # Lista para almacenar las columnas que cumplen con las condiciones
    columnas = []
    
    # Iteración sobre cada columna numérica, excluyendo aquellas con baja cardinalidad
    for col in dataframe.select_dtypes(include=np.number).columns:
        if len(dataframe[col].unique()) > 10:  # Se comprueba que tenga 10 valores o más para evitar añadir categóricas 'disfrazdas'
            relaciones = [dataframe[dataframe[target_col] == category][col].dropna() for category in dataframe[target_col].unique()]
            f_value, p_value = f_oneway(*relaciones)
            if p_value <= pvalue:
                columnas.append(col)
    
    return columnas


# FUNCION 3 JAIME
def plot_features_num_classification(dataframe, target_col="", columns=[], pvalue=0.05):
    """
    Genera pairplots entre las columnas numéricas 
    en el caso de que exista una relación estadística entre las mismas y columna target a través de ANOVA

    Argumentos:
    dataframe (pd.DataFrame): El DF seleccionado.
    target_col (str): La columna targert que es categórica.
    columns (list): Lista de nombres de columnas numéricas para incluir en el pairplot, lista vacía por defecto.
    pvalue (float): Valor p para la significancia estadística, 0.05 por defecto.

    Retorna:
    list: Nombres de las columnas incluidas en el pairplot.
    """
    
    # Comprobación de valores de entrada
    if not isinstance(dataframe, pd.DataFrame):
        print("El argumento 'dataframe' debe ser un DataFrame de pandas.")
        return None
    if not isinstance(target_col, str):
        print("El argumento 'target_col' debe ser una cadena de texto.")
        return None
    if not isinstance(columns, list):
        print("El argumento 'columns' debe ser una lista.")
        return None
    if not isinstance(pvalue, float):
        print("El argumento 'pvalue' debe ser un valor de punto flotante.")
        return None

    # Si no se proporcionan columnas, usar todas las numéricas
    if not columns:
        columns = dataframe.select_dtypes(include=np.number).columns.tolist()
    
   # Se llama a la función y esta hace el análsis ANNOVA
   # La función utliza los mismo parámetros de entrada
   # Ya se manejan las excepciones en la primera función 
    columnas_relacionadas = get_features_num_classification(dataframe, target_col, pvalue)
    
    # Filtrar columnas por las significativas
    columnas_pintar = [col for col in columns if col in columnas_relacionadas]
    # Aviso en el caso de que la lista esté vacía
    if not columnas_pintar:
        print("No hay columnas significativas.")
        return []
    
    # Pairplot
    sns.pairplot(dataframe, vars=columnas_pintar, hue=target_col) # pintar colores por cada categoría del target 
    plt.show()
    
    return columnas_pintar


def pinta_distribucion_categoricas(df, columnas_categoricas, relativa=False, mostrar_valores=False):
    num_columnas = len(columnas_categoricas)
    num_filas = (num_columnas // 2) + (num_columnas % 2)

    fig, axes = plt.subplots(num_filas, 2, figsize=(15, 5 * num_filas))
    axes = axes.flatten() 

    for i, col in enumerate(columnas_categoricas):
        ax = axes[i]
        if relativa:
            total = df[col].value_counts().sum()
            serie = df[col].value_counts().apply(lambda x: x / total)
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis', hue = serie.index, legend = False)
            ax.set_ylabel('Frecuencia Relativa')
        else:
            serie = df[col].value_counts()
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis', hue = serie.index, legend = False)
            ax.set_ylabel('Frecuencia')

        ax.set_title(f'Distribución de {col}')
        ax.set_xlabel('')
        ax.tick_params(axis='x', rotation=45)

        if mostrar_valores:
            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), 
                            ha='center', va='center', xytext=(0, 9), textcoords='offset points')

    for j in range(i + 1, num_filas * 2):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def plot_categorical_relationship_fin(df, cat_col1, cat_col2, relative_freq=False, show_values=False, size_group = 5):
    # Prepara los datos
    count_data = df.groupby([cat_col1, cat_col2]).size().reset_index(name='count')
    total_counts = df[cat_col1].value_counts()
    
    # Convierte a frecuencias relativas si se solicita
    if relative_freq:
        count_data['count'] = count_data.apply(lambda x: x['count'] / total_counts[x[cat_col1]], axis=1)

    # Si hay más de size_group categorías en cat_col1, las divide en grupos de size_group
    unique_categories = df[cat_col1].unique()
    if len(unique_categories) > size_group:
        num_plots = int(np.ceil(len(unique_categories) / size_group))

        for i in range(num_plots):
            # Selecciona un subconjunto de categorías para cada gráfico
            categories_subset = unique_categories[i * size_group:(i + 1) * size_group]
            data_subset = count_data[count_data[cat_col1].isin(categories_subset)]

            # Crea el gráfico
            plt.figure(figsize=(10, 6))
            ax = sns.barplot(x=cat_col1, y='count', hue=cat_col2, data=data_subset, order=categories_subset)

            # Añade títulos y etiquetas
            plt.title(f'Relación entre {cat_col1} y {cat_col2} - Grupo {i + 1}')
            plt.xlabel(cat_col1)
            plt.ylabel('Frecuencia' if relative_freq else 'Conteo')
            plt.xticks(rotation=45)

            # Mostrar valores en el gráfico
            if show_values:
                for p in ax.patches:
                    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', fontsize=10, color='black', xytext=(0, size_group),
                                textcoords='offset points')

            # Muestra el gráfico
            plt.show()
    else:
        # Crea el gráfico para menos de size_group categorías
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=cat_col1, y='count', hue=cat_col2, data=count_data)

        # Añade títulos y etiquetas
        plt.title(f'Relación entre {cat_col1} y {cat_col2}')
        plt.xlabel(cat_col1)
        plt.ylabel('Frecuencia' if relative_freq else 'Conteo')
        plt.xticks(rotation=45)

        # Mostrar valores en el gráfico
        if show_values:
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=10, color='black', xytext=(0, size_group),
                            textcoords='offset points')

        # Muestra el gráfico
        plt.show()


def plot_categorical_numerical_relationship(df, categorical_col, numerical_col, show_values=False, measure='mean'):
    # Calcula la medida de tendencia central (mean o median)
    if measure == 'median':
        grouped_data = df.groupby(categorical_col)[numerical_col].median()
    else:
        # Por defecto, usa la media
        grouped_data = df.groupby(categorical_col)[numerical_col].mean()

    # Ordena los valores
    grouped_data = grouped_data.sort_values(ascending=False)

    # Si hay más de 5 categorías, las divide en grupos de 5
    if grouped_data.shape[0] > 5:
        unique_categories = grouped_data.index.unique()
        num_plots = int(np.ceil(len(unique_categories) / 5))

        for i in range(num_plots):
            # Selecciona un subconjunto de categorías para cada gráfico
            categories_subset = unique_categories[i * 5:(i + 1) * 5]
            data_subset = grouped_data.loc[categories_subset]

            # Crea el gráfico
            plt.figure(figsize=(10, 6))
            ax = sns.barplot(x=data_subset.index, y=data_subset.values)

            # Añade títulos y etiquetas
            plt.title(f'Relación entre {categorical_col} y {numerical_col} - Grupo {i + 1}')
            plt.xlabel(categorical_col)
            plt.ylabel(f'{measure.capitalize()} de {numerical_col}')
            plt.xticks(rotation=45)

            # Mostrar valores en el gráfico
            if show_values:
                for p in ax.patches:
                    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                                textcoords='offset points')

            # Muestra el gráfico
            plt.show()
    else:
        # Crea el gráfico para menos de 5 categorías
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=grouped_data.index, y=grouped_data.values)

        # Añade títulos y etiquetas
        plt.title(f'Relación entre {categorical_col} y {numerical_col}')
        plt.xlabel(categorical_col)
        plt.ylabel(f'{measure.capitalize()} de {numerical_col}')
        plt.xticks(rotation=45)

        # Mostrar valores en el gráfico
        if show_values:
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Muestra el gráfico
        plt.show()


def plot_combined_graphs(df, columns, whisker_width=1.5, bins = None):
    num_cols = len(columns)
    if num_cols:
        
        fig, axes = plt.subplots(num_cols, 2, figsize=(12, 5 * num_cols))
        print(axes.shape)

        for i, column in enumerate(columns):
            if df[column].dtype in ['int64', 'float64']:
                # Histograma y KDE
                sns.histplot(df[column], kde=True, ax=axes[i,0] if num_cols > 1 else axes[0], bins= "auto" if not bins else bins)
                if num_cols > 1:
                    axes[i,0].set_title(f'Histograma y KDE de {column}')
                else:
                    axes[0].set_title(f'Histograma y KDE de {column}')

                # Boxplot
                sns.boxplot(x=df[column], ax=axes[i,1] if num_cols > 1 else axes[1], whis=whisker_width)
                if num_cols > 1:
                    axes[i,1].set_title(f'Boxplot de {column}')
                else:
                    axes[1].set_title(f'Boxplot de {column}')

        plt.tight_layout()
        plt.show()

def plot_grouped_boxplots(df, cat_col, num_col):
    unique_cats = df[cat_col].unique()
    num_cats = len(unique_cats)
    group_size = 5

    for i in range(0, num_cats, group_size):
        subset_cats = unique_cats[i:i+group_size]
        subset_df = df[df[cat_col].isin(subset_cats)]
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=cat_col, y=num_col, data=subset_df)
        plt.title(f'Boxplots of {num_col} for {cat_col} (Group {i//group_size + 1})')
        plt.xticks(rotation=45)
        plt.show()



def plot_grouped_histograms(df, cat_col, num_col, group_size, bins = "auto"):
    unique_cats = df[cat_col].unique()
    num_cats = len(unique_cats)

    for i in range(0, num_cats, group_size):
        subset_cats = unique_cats[i:i+group_size]
        subset_df = df[df[cat_col].isin(subset_cats)]
        
        plt.figure(figsize=(10, 6))
        for cat in subset_cats:
            sns.histplot(subset_df[subset_df[cat_col] == cat][num_col], kde=True, label=str(cat), bins = bins)
        
        plt.title(f'Histograms of {num_col} for {cat_col} (Group {i//group_size + 1})')
        plt.xlabel(num_col)
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()



def grafico_dispersion_con_correlacion(df, columna_x, columna_y, tamano_puntos=50, mostrar_correlacion=False):
    """
    Crea un diagrama de dispersión entre dos columnas y opcionalmente muestra la correlación.

    Args:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    columna_x (str): Nombre de la columna para el eje X.
    columna_y (str): Nombre de la columna para el eje Y.
    tamano_puntos (int, opcional): Tamaño de los puntos en el gráfico. Por defecto es 50.
    mostrar_correlacion (bool, opcional): Si es True, muestra la correlación en el gráfico. Por defecto es False.
    """

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=columna_x, y=columna_y, s=tamano_puntos)

    if mostrar_correlacion:
        correlacion = df[[columna_x, columna_y]].corr().iloc[0, 1]
        plt.title(f'Diagrama de Dispersión con Correlación: {correlacion:.2f}')
    else:
        plt.title('Diagrama de Dispersión')

    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.grid(True)
    plt.show()


def bubble_plot(df, col_x, col_y, col_size, scale = 1000):
    """
    Crea un scatter plot usando dos columnas para los ejes X e Y,
    y una tercera columna para determinar el tamaño de los puntos.

    Args:
    df (pd.DataFrame): DataFrame de pandas.
    col_x (str): Nombre de la columna para el eje X.
    col_y (str): Nombre de la columna para el eje Y.
    col_size (str): Nombre de la columna para determinar el tamaño de los puntos.
    """

    # Asegúrate de que los valores de tamaño sean positivos
    sizes = (df[col_size] - df[col_size].min() + 1)/scale

    plt.scatter(df[col_x], df[col_y], s=sizes)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f'Burbujas de {col_x} vs {col_y} con Tamaño basado en {col_size}')
    plt.show()


