<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL N°2** </h1>
# <h2 align=center> ** Víctimas de Siniestros Viales en CABA ** </h2>


# <h2 align=center>**INTRODUCCION**</h2>

<p style="text-indent: 20px;">
En este proyecto se simula el rol de un Data Analyst de una empresa consultora para la que el Observatorio de Movilidad y Seguridad Vial (OMSV), organismo que depende de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), le solicitó la elaboración de un proyecto de análisis de datos.
</p>

<p style="text-indent: 20px;">
Como finalidad, se busca generar información que permita disminuir la cantidad de víctimas fatales de los siniestros viales ocurridos en CABA. Para ello, se pone a disposición un dataset sobre homicidios en siniestros viales de en la Ciudad de Buenos Aires durante el periodo 2016-2021.
</p>

<p style="text-indent: 20px;">
Se espera como productos finales un reporte de las tareas realizadas, metodologías adoptadas y principales conclusiones y la presentación de un dashboard interactivo que facilite la interpretación de la información y su análisis.
</p>



# <h2 align=center>**CONTEXTO**</h2>

<p style="text-indent: 20px;">
En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales. Aunque muchas jurisdicciones han logrado disminuir la cantidad de accidentes de tránsito, esta sigue siendo la principal causa de muertes violentas en el país. Los informes del Sistema Nacional de Información Criminal (SNIC), del Ministerio de Seguridad de la Nación, revelan que entre 2018 y 2022 se registraron 19.630 muertes en siniestros viales en todo el país. Estas cifras equivalen a 11 personas por día que resultaron víctimas fatales por accidentes de tránsito.
</p>

<p style="text-indent: 20px;">
Solo en 2022, se contabilizaron 3.828 muertes fatales en este tipo de hechos. Los expertos en la materia indican que en Argentina es dos o tres veces más alta la probabilidad de que una persona muera en un siniestro vial que en un hecho de inseguridad delictiva.
</p>

<p style="text-indent: 20px;">
La Ciudad Autónoma de Buenos Aires, que se ubica en la provincia de Buenos Aires en Argentina, no es la excepción a esta problemática, sino que los siniestros viales son una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener un impacto significativo en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia.
</p>

<p style="text-indent: 20px;">
Actualmente, según el censo poblacional realizado en el año 2022, la población de CABA es de 3,120,612 de habitantes en una superficie de 200 km<sup>2</sup>, lo que implica una densidad de aproximadamente 15,603 hab/km<sup>2</sup> <a href=https://www.argentina.gob.ar/caba#:~:text=Poblaci%C3%B3n%3A%203.120.612%20habitantes%20(Censo%202022).>(Fuente)</a>. Sumado a esto, el Julio de 2023 se registraron 12,437,735 de vehículos transitando por los peajes de las autopistas de acceso a CABA <a href=https://www.estadisticaciudad.gob.ar/eyc/?p=41995.>(Fuente)</a>. Por lo que la prevención de siniestros viales y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.
</p>



# <h2 align=center>**DATOS**</h2>

<p style="text-indent: 20px;">
Para este proyecto se trabajó con la Bases de Víctimas Fatales en Siniestros Viales que se encuentra en formato de Excel y contiene dos pestañas de datos:

* HECHOS: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
* VICTIMAS: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. 

Se vincula a los HECHOS mediante el id del hecho.
</p>

<p style="text-indent: 20px;">
Tales datos fueron extraídos del siguiente <a href=https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales>link</a> del Gobierno de la Ciudad de Buenos Aires
y en este <a href=https://github.com/leoviscay/PI2_Siniestros-Viales/blob/main/data/NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf>documento</a> se detallan todas las definiciones manejadas en los datos y en el desarrollo de este proyecto. 
</p>



# <h2 align=center>**ETL y EDA**</h2>
<h4 align=center>(Extracción, Transformación y Carga de Datos) y (Análisis Exporatorio de Datos)</h4>

<p style="text-indent: 20px;">
En este proyecto se utilizó Python y Pandas para los procesos de extracción, transformación y carga de los datos, como así también para el análisis exploratorio de los datos. En el siguiente apartado se describen los resultados del análisis.
</p>

<p style="text-indent: 20px;">
Luego, para la obtención complementaria de datos para el cálculo de la población en el año 2021 se realizó webscraping utilizando la librería BeautifulSoup. Este proceso puede visualizarse en el siguiente <a href=<a href=https://github.com/leoviscay/PI2_Siniestros-Viales/blob/main/data/NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf>documento</a>.
</p>

<p style="text-indent: 20px;">
En primer lugar, se realizó un proceso de extracción, transformación y carga de los datos (ETL), tanto de "HECHOS" como "VÍCTIMAS", donde se estandarizaron nombres de las variables, se analizaron nulos y duplicados de los registros, se eliminaron columnas redundantes o con muchos valores faltantes, entre otras tareas. Una vez finalizado este proceso para los dos conjuntos de datos de "Homicidios" se procedió a unir los dos conjuntos en uno solo denominado df_homicidios.
</p>

<p style="text-indent: 20px;">
En segundo lugar, se procedió a realizar un análisis exploratorio exahustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. Todos los detalles de este análisis se encuentran <a href=<a href=https://github.com/leoviscay/PI2_Siniestros-Viales/blob/main/jupyter/ETL_EDA_Homicidios.ipynb>aqui</a>..
</p>

<p style="text-indent: 20px;">
Finalmente, para la construcción de un dashboard interactivo se utiliza Power BI, el cuál se puede consultar <a href=<a href=https://github.com/leoviscay/PI2_Siniestros-Viales/blob/main/Dashboard_PI2.pbix>aqui</a>.
</p>

<p style="text-indent: 20px;">

</p>



