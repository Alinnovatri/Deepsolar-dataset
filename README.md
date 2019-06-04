
[![MIT Software License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE.md)

# Documentation
* [Descripción del proyecto](#DeepSolar-Dataset)
    - [Contexto](#Contexto)
    - [¿Cómo comenzar?](#Comenzando)
        - [Pre-requisitos](#Pre-requisitos)
        - [Versiones de librerias utilizadas](#Versiones de librerias utilizadas)
    - [Métodos del programa](#Métodos del programa)
     

# DeepSolar Dataset
_Análisis de un conjunto de datos del proyecto DeepSolar de Stanford._

## Contexto

_Se realizará un análisis del conjunto de datos adquiridos a partir del proyecto DeepSolar de Standford el cual se encarga de realizar un análisis de imágenes satelitales para identificar el tamaño y ubicación de paneles fotovoltaicos en los Estados Unidos de América (EE. UU)._  

## ¿Cómo comenzar? 

_Para realizar una copìa de este repositorio es necesario seguir los suquientes pasos: _

### Pre-requisitos

Libreria de pandas para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
conda install -c anaconda pandas 
```


Libreria de matplotlib para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge matplotlib 
```


Libreria de seaborn para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge seaborn 
```


Libreria de numpy para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge numpy 
```

Libreria de scipy para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge scipy 
```



Libreria de sklearn para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge sklearn-contrib-lightning 
 ```


Libreria de basemap para anaconda. Ejecute el siguiente comando en su terminal en anaconda:

```
 conda install -c conda-forge basemap 
 ```



### Versiones de librerias utilizadas
```
alabaster                 0.7.12                   py36_0
anaconda-client           1.7.2                    py36_0
anaconda-navigator        1.9.7                    py36_0
anaconda-project          0.8.2                    py36_0
clyent                    1.2.2                    py36_1
colorama                  0.3.9            py36hd29a30c_0
conda                     4.4.10                   py36_0
conda-build               3.4.1                    py36_0
conda-env                 2.6.0                h36134e3_0
conda-verify              2.0.0            py36he837df3_0
contextlib2               0.5.5            py36hd66e5e7_0
cryptography              2.3.1            py36hdbc3d79_0
curl                      7.61.1               ha441bb4_00
dbus                      1.13.6               h90a0687_0
decorator                 4.4.0                    py36_1
defusedxml                0.6.0                      py_0
descartes                 1.1.0                    py36_0
distributed               1.20.2                   py36_0
docutils                  0.14             py36hbfde631_0
entrypoints               0.3                      py36_0
et_xmlfile                1.0.1            py36h1315bdc_0
expat                     2.2.6                h0a44026_0
fontconfig                2.13.0               h5d5b041_1
freetype                  2.9.1                hb4e5f40_0
freexl                    1.0.5                h1de35cc_0
gdal                      2.2.2            py36hd505dc6_1
geopandas                 0.4.1                      py_0
geos                      3.6.2                h5470d99_2
git                       2.19.1          pl526h028e6c8_0
gitdb2                    2.0.5                    py36_0
gitpython                 2.1.11                   py36_0
glib                      2.56.2               hd9629dc_0
glob2                     0.6              py36h94c9186_0
gmp                       6.1.2                hb37e062_1
gmpy2                     2.0.8            py36hf9c35bd_2
greenlet                  0.4.12           py36hf09ba7b_0
h5py                      2.7.1            py36h39cdac5_0
hdf4                      4.2.13               h39711bb_2
hdf5                      1.10.1               ha036c08_1
heapdict                  1.0.0                    py36_2
html5lib                  1.0.1                    py36_0
icu                       58.2                 h4b95b61_1
cac_0
ipython_genutils          0.2.0            py36h241746c_0
ipywidgets                7.1.1                    py36_0
isort                     4.2.15           py36hceb2a01_0
itsdangerous              0.24             py36h49fbb8d_1
jbig                      2.1                  h4d881f8_0
jdcal                     1.3              py36h1986823_0
jedi                      0.13.3                   py36_0
jinja2                    2.10.1                   py36_0
jpeg                      9b                   he5867d9_2
json-c                    0.13.1               h3efe00b_0
jsonschema                3.0.1                    py36_0
jupyter                   1.0.0                    py36_4
jupyter_client            5.2.4                    py36_0
jupyter_console           5.2.0            py36hccf5b1c_1
jupyter_core              4.4.0                    py36_0
jupyterlab                0.35.5           py36hf63ae98_0
jupyterlab-git            0.5.0                      py_1   
jupyterlab_launcher       0.13.1                   py36_0
jupyterlab_server         0.2.0                    py36_0
markupsafe                1.1.1            py36h1de35cc_0
matplotlib                3.1.0            py36h54f8f79_0
matplotlib-base           3.1.0            py36h3a684a6_1    
mccabe                    0.6.1            py36hdaeb55d_0
mistune                   0.8.4            py36h1de35cc_0
mkl                       2019.4                      233
mkl-service               2.0.2            py36h1de35cc_0
mpc                       1.0.3                h7a72875_5
mpfr                      3.1.5                h711e7fd_2
mpmath                    1.0.0            py36hf1b8295_2
msgpack-python            0.5.1            py36h04f5b5a_0
multipledispatch          0.4.9            py36hc5f92b5_0
munch                     2.3.2                    py36_0
navigator-updater         0.1.0            py36h7aee5fb_0
nbconvert                 5.5.0                      py_0
nbformat                  4.4.0            py36h827af21_0
nodejs                    10.13.0              h0a44026_0
nose                      1.3.7                    py36_2
notebook                  5.7.8                    py36_0
numba                     0.36.2          np114py36hc2f221f_0
numexpr                   2.6.4            py36habcfcfe_0
numpy                     1.14.6           py36ha462648_4
numpy-base                1.14.6           py36ha711998_4
numpydoc                  0.9.1                      py_0
odo                       0.5.1            py36hc1af34a_0
olefile                   0.46                     py36_0
openblas                  0.3.5             h436c29b_1001   
openjpeg                  2.3.0                hb95cd4c_1
openpyxl                  2.4.10                   py36_0
openssl                   1.0.2s               h1de35cc_0
packaging                 19.0                     py36_0
pandas                    0.24.2           py36h0a44026_0
pandoc                    2.2.3.2                       0
pandocfilters             1.4.2                    py36_1
parso                     0.4.0                      py_0
partd                     0.3.8            py36hf5c4cb8_0
path.py                   12.0.1                     py_0
pathlib2                  2.3.3                    py36_0
patsy                     0.5.0                    py36_0
pcre                      8.43                 h0a44026_0
pep8                      1.7.1                    py36_0
perl                      5.26.2               h4e221da_0
pexpect                   4.7.0                    py36_0
prompt_toolkit            2.0.9                    py36_0
psutil                    5.6.2            py36h1de35cc_0
psycopg2                  2.7.5            py36hdbc3d79_0
ptyprocess                0.6.0                    py36_0
py                        1.5.2            py36ha69170d_0
pycodestyle               2.3.1            py36h83e8646_0
pycosat                   0.6.3            py36hee92d8f_0
pycparser                 2.19                     py36_0
python                    3.6.6                hc167b69_0
pytz                      2019.1                     py_0


```

## Métodos del programa 


```
showParamData(self)       -> La función devuelve las variables que se consideraron en el proyecto Deep Solar
showCantColuRow(self)     -> La función devuelve el número total de filas y columnas que se consideraron en el proyecto Deep Solar.
showHistCantSolarSys(self,limINF=20,limSUP=200) -> La función devuelve un histograma en el que se muestra la frecuencia de la cantidad de paneles fotovoltaicos que fueron contados en los 
                                                   Estados Unidos. Se pueden establecer rangos de visualización delos parámetros que va desde 0 hasta 4000 que corresponden al mínimo y 
                                                   máximo de paneles.
```

```
showHistPaneAreaPerCap(self,limINF=0.1,limSUP=0.6) -> La función devuelve un histograma en el que se muestra la frecuencia de la cantidad de paneles fotovoltaicos que fueron contados en los
                                                      Estados Unidos. Se pueden establecer rangos de visualización delos parámetros que va desde 0 hasta 1 que corresponden al mínimo y máximo 
                                                      de paneles
```


```
showBarGraphSector(self)  ->La función devuelve una una gráfica de barras apiladas que represneta el total de paneles y sistemas solares en el que se especifica el sector por uso residencial 
                            y no residencial.
```
```
showCorreFacVarSol(self)  -> La función devuelve una una gráfica en la que se hace una correlación entre las variables ambientales y ecónomicas por lad e incentivos que hay para la 
            implemetación cantidad de sistemas y paneles fotovoltaicos.
            Los factores con la correlación positiva más fuerte tienen cuadrados que tienen un color azul oscuro y los de menor con un color claro.
```
```
showCorrFacSociEco(self)  ->La función devuelve una una gráfica en la que se hace una correlación entre las variables socioecónomicas por la cantidad de incentivos que hay para la 
            implemetación de sistemas y paneles fotovoltaicos .
            Los factores con la correlación positiva más fuerte tienen cuadrados que tienen un color verde acuoso y los de menor con un color azul oscuro.
```