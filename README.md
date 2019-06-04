
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
Da un ejemplo
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