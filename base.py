import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st

base_of = pd.read_csv("Base_oficial__sin_filtro.csv")
base_of.loc[base_of['CodigoSerieHidrologica'] == 'ALICBOGO', 'RegionHidrologica'] = 'Centro'
base_of.dropna(inplace=True)

# Crear pestañas
tab1, tab2, tab3, tab4= st.tabs(["Descripción", "Base de datos", "Limpieza", "Visualización"])


# Contenido de la primera pestaña
with tab1: 
    st.title("Proyecto Grupo 2")
    st.markdown(f'''**Breve descripción:** Dada la gran relevancia de las energías renovables 
                a nivel mundial, Colombia se ha encamindo a construir una relación directa con la energía hídrica,
                base importante del sistema energético nacional.  Este proyecto tiene como principal objetivo analizar 
                el aporte energético de algunas fuentes hídricas ubicadas en  diferentes regiones del país entre el año 
                2019 al 2024. \nDocumentación oficial del proyecto en este [enlace](https://docs.google.com/document/d/1n6q818P3u3SP_zAPgCsf90acUZrU_f-vM8FBaTLnppo/edit?usp=sharing)
                ''')

# Contenido de la segunda pestaña
with tab2:
    st.subheader("Base de datos")
    st.markdown(f'''**Descripción:** Esta base de datos cuenta con diferentes registros sobre los aportes energéticos
                de diferentes fuentes hídricas del país al Sistema Interconectado Nacional. Fue necesario realizar diferentes concatenaciones de varias bases de datos,
                a conitnuación se presenta la descripción de este proceso
                \n**Fuente:** [Enlace a la base de datos](https://www.datos.gov.co/dataset/Aportes-Hidr-ulicos-Energ-a/wa2n-56u4/about_data)   
                ''')
    st.write(base_of)

    st.subheader("Concatenación")
    codigo = '''input_path_file = '/content/drive/MyDrive/Programación/Talento tech/Proyecto/Metan las BD/' ## Carpeta con las bases a concatenar
    output_path_file = '/content/drive/MyDrive/Programación/Talento tech/Proyecto/' ## Carpeta dónde extraer la base de datos concatenada

    excel_file_list = os.listdir(input_path_file)
    excel_file_list.sort() ## Organizar las bases de datos del menor año al mayor
    excel_file_list
    df_of = pd.DataFrame()

    for i in excel_file_list:
      df = pd.read_csv(input_path_file + i)
      df_of = pd.concat([df_of, df], ignore_index = True)

    df_of'''
    st.markdown("""El proceso de concatenación de bases de datos tuvo cómo base los siguientes pasos:
                \n1. **Escogencia de los datos:** Para obtener una buena visualización de los datos, y lograr el análisis adecuado de estos, hemos escogido los días primero de cada mes a lo largo de los años 2019 al 2024.
                \n2. **Descarga:** Se ha escogido una fuente de Datos Abiertos, sin embargo, fue necesario descargar cada dia en un csv por separado. Fuente: https://www.simem.co/datadetail/2bff145f-a233-4644-b5eb-74188dfba51c
                \n3. **Concatenación:** Realizamos una concatenación anual y luego otra sobre las bases de datos de cada año (para evitar sobrecarga del collab omitimos la primera concatenación).
                \n4. **Continuación:** Posteriormente procedemos a hacer uso de funciones de estadística descriptiva, limpieza y visualización de los datos.""")

    st.code(codigo)

    st.subheader("Exploración")
    st.text("Haciendo uso de la estadística descriptiva realizaremos una exploración\ninicial del Dataset")
    st.markdown(f"La cantidad total de registros es: `{len(base_of)}`")
    st.markdown(f"La cantidad total de columnas es: ``")
    st.code("base_of.describe()")
    st.write(base_of.describe())
    st.code("base_of.info()")
    st.dataframe(base_of.info())
    st.markdown(f"A continuación brindamos información útil sobre las columnas de nuestro Dataset")
    df_info = pd.DataFrame({
        "Columnas":["FechaPublicacion", "Fecha", "CodigoDuracion", "CodigoSerieHidrologica", "RegionHidrologica", "AportesHidricosEnergia", "PromedioAcumuladoEnergia", "MediaHistoricaEnergia", "AportesHidricosEnergiaPSS95"],
        "Descripción": ["Fecha de publicación del dato en el SIMEM",
                        "Fecha de representación de la información",
                        "Código de duración de la variable en formato ISO8601",
                        "Código único para identificar una serie hidrologica o un río del Sistema Interconectado Nacional",
                        "Zona geográfica en la cual se agrupan elementos con características hidrológicas similares",
                        "Aporte hídrico asociado con un recurso de generación despachado centralmente en kWh",
                        "Aportes hidricos promedio para lo que va corrido del mes en kWh",
                        "Promedio mensual multianual de la serie hidrológica aprobada por Acuerdo CNO en kWh",
                        "Hidrología al 95% (en kWh)"],
        "Tipo": ["Fecha", "Fecha", "Texto", "Texto", "Texto", "Decimal", "Decimal", "Decimal", "Decimal"]})
    st.write(df_info)
    
# Contenido de la tercera pestaña
with tab3:
    st.subheader("Limpieza")
    st.markdown("Procederemos a realizar la limpieza de los datos, primero conozcamos sobre los datos nulos dentro del DataFrame")

    st.write(base_of.isnull().sum())
    st.markdown("Analicemos el siguiente filtro, se pueden notar registros que a pesar de tener el mismo Codigo cuentan con una region Nula.")
    st.write(base_of[base_of["CodigoSerieHidrologica"]=="ALICBOGO"])
    st.markdown("Hemos cambiado los valores nulos por la region correspondiente.")
    base_of.loc[base_of['CodigoSerieHidrologica'] == 'ALICBOGO', 'RegionHidrologica'] = 'Centro'
    st.write(base_of[base_of["CodigoSerieHidrologica"]=="ALICBOGO"])
    st.markdown("Debido a que el Dataset cuenta con gran cantidad de datos podemos eliminar aquellos datos nulos que no aportan al estudio.")

    base_of.dropna(inplace=True)
    st.write(base_of)
    st.markdown(f"La cantidad total de registros después de la limpueza es: `{len(base_of)}`\n Comprobemos que no queden valores nulos, así: ")
    st.code("base_of.isnull().sum()")
    st.write(base_of.isnull().sum())
    
# Contenido de la cuarta pestaña
"""with tab4:
    st.header("Visualización")

    base_ant = base_of[base_of["RegionHidrologica"]=="Antioquia"]
    st.write(base_ant["CodigoSerieHidrologica"].value_counts())
    base_hola = base_ant.iloc[:, [3, 5, 6, 7, 8]].groupby("CodigoSerieHidrologica").mean()["AportesHidricosEnergia"]
    st.write(base_hola)


    df_fuentes = pd.read_csv("FuentesHidricas.csv")
    df_join = base_ant.join(df_fuentes.set_index('CodigoSerieHidrologica'), on='CodigoSerieHidrologica')
    st.write(df_join)
    df_group = df_join.iloc[:, [-3, 5, 6, 7, 8]].groupby("FuentesHidricas").mean().loc[:, "AportesHidricosEnergia": "AportesHidricosEnergiaPSS95"]
    st.write(df_group)
    st.line_chart(df_group["AportesHidricosEnergia"])

    st.map(df_join, latitude='Latitud', longitude='Longitud', size= 1000)

    df_region = base_of.iloc[:, [4, 5, 6, 7, 8]].groupby("RegionHidrologica").mean().loc[:, "AportesHidricosEnergia": "AportesHidricosEnergiaPSS95"]
    st.write(df_region)
    st.bar_chart(df_region["AportesHidricosEnergia"])
    st.write()"""