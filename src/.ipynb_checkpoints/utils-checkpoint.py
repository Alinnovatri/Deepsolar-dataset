#Se implementan la librerias necesarios 
import os             
import numpy as np     
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import scipy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
# Librerias necesarias para realizar el  mapa de correlaciones
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon


#Ignoramos Warnings
np.warnings.filterwarnings('ignore')
print("Se importaron las librerías necesarias.")



class DeepSolar: 
        """
        Te permite visualizar y realizar un análisis de la implementación de la energía solar fotovoltaica en los Estados Unidosa partir de los datos del proyecto 
        Deep Solar por la Universidad de Standford el cual consiste en identificar aspectos relacionados con paneles fotovoltaicos en el país así como ambientales y 
        socioeconómicos.
        
        """
        
        
        def __init__(self, file):
            """
            La función devuelve un DataFrame con las variables que se consideraron en el proyecto Deep Solar en el que se remplazan los valores
            NA en cada columna de datos con la media de la columna.No se requiere establecer un index ya que se realizaran correlaciones entre los datos. 
                
            Parámetros:
                    file -- ruta donde se encuentra el archivo csv con la información del proyecto Deep Solar

            """
            #Lectura del archivo CSV mediante pandas y un dataframe. Se realiza una modificación en el tipo de codificación, esto se debe 
            #a que los datos tienen un formato latin-1. 
            self.data = pd.read_csv(file, encoding='latin-1')
            #Ramplaza todos los valores de NA en cada columna de datos con la media de la columna
            self.data.fillna(self.data.mean());
           
        
        def showParamData(self):
            """
            La función devuelve las variables que se consideraron en el proyecto Deep Solar
            """
            print(len(list(self.data.columns.values)),list(self.data.columns.values));
        
        def showCantColuRow(self):
            """
            La función devuelve el número total de filas y columnas que se consideraron en el proyecto Deep Solar.
            """
            # Regresa el número total de filas y columnas
            print("EL dataset tiene " + str(self.data.shape[0]) + " filas y " + str(self.data.shape[1]) + " columnas.")
       
        def showHistCantSolarSys(self,limINF=20,limSUP=200):
            """
            La función devuelve un histograma en el que se muestra la frecuencia de la cantidad de paneles fotovoltaicos que fueron contados en los
            Estados Unidos. Se pueden establecer rangos de visualización delos parámetros que va desde 0 hasta 4000 que corresponden al mínimo y máximo de paneles.
                
            Parámetros:
                    limINF[int] -- Límite inferior del rango de visualización 
                    limSUP[int] -- Límite superior del rango de visualización 
                
            """
            fig, ax = plt.subplots(figsize=(20, 10))
            # Método para determinar el número de clases que se deben considerar mediante el la regla de Sturges
            plt.hist(self.data['tile_count'], math.ceil((limSUP-limINF)/ (math.sqrt(limSUP-limINF))) ,
                     range=[limINF, limSUP],edgecolor = 'black',linewidth=1, facecolor='aquamarine')
            plt.title('Frecuencia de la cantidad de paneles fsotovoltaicos')
            plt.show()
        
        def showHistPaneAreaPerCap(self,limINF=0.1,limSUP=0.6):
            """
            La función devuelve un histograma en el que se muestra la frecuencia de la cantidad de paneles fotovoltaicos que fueron contados en los
            Estados Unidos. Se pueden establecer rangos de visualización delos parámetros que va desde 0 hasta 1 que corresponden al mínimo y máximo de paneles.

            Parámetros:
                    limINF[float] -- Límite inferior del rango de visualización 
                    limSUP[float] -- Límite superior del rango de visualización 

            """
            fig, ax = plt.subplots(figsize=(20, 10))
            # Método para determinar el número de clases que se deben considerar mediante el la regla de Sturges
            plt.hist(self.data['solar_panel_area_per_capita'], 35, 
                     range=[limINF, limSUP], facecolor='aquamarine',edgecolor = 'black',linewidth=1)
            plt.title('Frecuencia del área del panel solar per cápita')

            plt.show()
        
        def showBarGraphSector(self):
            """
            La función devuelve una una gráfica de barras apiladas que represneta el total de paneles y sistemas solares en el que se especifica el sector por uso residencial y no residencial.
            """
            fig, ax = plt.subplots(figsize=(20, 10))

            total_tile = int(self.data['tile_count'].sum())
            total_system = int(self.data['solar_system_count'].sum())
            barstotal = [total_tile, total_system]

            count_residential = int(self.data['tile_count_residential'].sum())
            count_nonresidential = int(self.data['tile_count_nonresidential'].sum())

            solar_system_count_residential =int(self.data['solar_system_count_residential'].sum())
            solar_system_count_nonresidential = int(self.data['solar_system_count_nonresidential'].sum())

            N = 2
            bar1 = (count_residential,solar_system_count_residential )
            bar2 = (count_nonresidential, solar_system_count_nonresidential)

            ind = np.arange(N)  
            width = 0.8       

            p1 = plt.bar(ind, bar1, width, facecolor='darkblue')
            p2 = plt.bar(ind, bar2, width, bottom=bar1, facecolor='teal')

            plt.ylabel('Cantidad')
            plt.title('Uso residencial y no residencial de energía solar')
            plt.xticks(ind, ('Paneles Fotovoltaicos', 'Sistemas solares'))
            plt.legend((p1[0], p2[0]), ('Uso residencial', 'No Residencial'))
            plt.show()
        

        def showCorreFacVarSol(self):
            """
            La función devuelve una una gráfica en la que se hace una correlación entre las variables ambientales y ecónomicas por lad e incentivos que hay para la 
            implemetación cantidad de sistemas y paneles fotovoltaicos.
            Los factores con la correlación positiva más fuerte tienen cuadrados que tienen un color azul oscuro y los de menor con un color claro.

            """
            fig, ax = plt.subplots(figsize=(20, 20))

            #define columns to find correlations  
            energyenv_quant_data = ["total_panel_area", "total_panel_area_residential", "total_panel_area_nonresidential","electricity_price_overall",
                                    "avg_electricity_retail_rate", "electricity_consume_total", "incentive_count_residential", "incentive_count_nonresidential", 
                                    "heating_fuel_gas_rate", "heating_fuel_solar_rate","daily_solar_radiation",  "air_temperature",]

            sns.set_context("poster")
            # RdYlBu_r
            sns.set(font_scale=1.3)
            corrmap = sns.color_palette("Blues", 100)
            sns.heatmap(self.data[energyenv_quant_data].corr(),annot=True, fmt='.2f',linewidths=1,cmap = corrmap)
        
        
        def showCorrFacSociEco(self):
            """
            La función devuelve una una gráfica en la que se hace una correlación entre las variables socioecónomicas por la cantidad de incentivos que hay para la 
            implemetación de sistemas y paneles fotovoltaicos .
            Los factores con la correlación positiva más fuerte tienen cuadrados que tienen un color verde acuoso y los de menor con un color azul oscuro.
            """
            fig, axe = plt.subplots(figsize=(20, 20))
            socioecon_quant_data = ["total_panel_area", "total_panel_area_residential", "median_household_income","number_of_years_of_education", 
                                    "age_median", "poverty_family_count", "per_capita_income", "population_density", "employ_rate", "gini_index", "diversity",
                                    "voting_2016_dem_percentage", 'voting_2016_gop_percentage']

            sns.set_context("poster")

            sns.set(font_scale=1.3)
            colmap2 = sns.color_palette("GnBu_d", 100)
            sns.heatmap(self.data[socioecon_quant_data].corr(),annot=True, fmt='.2f',linewidths=1,cmap = colmap2)


        
#df2 = data.groupby('state').total_panel_area.sum()
#df2 = df2.to_frame()