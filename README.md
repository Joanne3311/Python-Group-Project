# Python-Group-Project
!pip install eikon
import eikon
import datetime

import refinitiv.data.eikon as ek
from IPython.display import HTML
ek.set_app_key('1131f92f9ebc4ec3870206fdf495a52af08a3795')
import refinitiv.data as rd
import numpy as np
import pandas as pd
import matplotlib as plt
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline

# Ignorer les avertissements
warnings.filterwarnings("ignore")

# Récupération des données pour un stock spécifique
stock_symbol = 'LVMH.PA'  # Remplacez 'AAPL' par le symbole ou le code du stock que vous souhaitez afficher
df_single_stock = rd.get_data(stock_symbol, ['TR.TRBCEconomicSector', 'TR.F.SalesPerEmp(Period=FY0)',
                              'TR.AnalyticEnergyUse(Period=FY0)', 'TR.CO2EmissionTotal(Period=FY0)',
                              'TR.CO2IndirectScope3(Period=FY0)', 'TR.EnergyUseTotal(Period=FY0)', 'TR.DividendYield'])

# Renommage des colonnes
df_single_stock.columns = ['Instrument', 'Sector', 'Revenue/Employee', 'EnergyUse/Revenue', 'CO2Emissions', 'CO2EmissionsScope3',
               'EnergyUse', 'DividendYield']

# Calculs supplémentaires
df_single_stock['CO2PerYield'] = (df_single_stock['CO2Emissions'] + df_single_stock['CO2EmissionsScope3'])  / df_single_stock['DividendYield']
df_single_stock['CO2Emissions/EnergyUse'] = df_single_stock['CO2Emissions'] / df_single_stock['EnergyUse']
df_single_stock['CO2Scope12/EnergyUse'] = df_single_stock['CO2Emissions'] / df_single_stock['EnergyUse']
df_single_stock['CO2Scope123/EnergyUse'] = (df_single_stock['CO2Emissions'] + df_single_stock['CO2EmissionsScope3']) / df_single_stock['EnergyUse']

# Conversion des colonnes pertinentes en données numériques
df_single_stock['Revenue/Employee'] = pd.to_numeric(df_single_stock['Revenue/Employee'], errors='coerce')
df_single_stock['EnergyUse/Revenue'] = pd.to_numeric(df_single_stock['EnergyUse/Revenue'], errors='coerce')
df_single_stock['CO2Emissions/EnergyUse'] = pd.to_numeric(df_single_stock['CO2Emissions/EnergyUse'], errors='coerce')
df_single_stock['CO2Scope123/EnergyUse'] = pd.to_numeric(df_single_stock['CO2Scope123/EnergyUse'], errors='coerce')

# Calculs
df_single_stock['CEIScope12'] = df_single_stock['Revenue/Employee'] * df_single_stock['EnergyUse/Revenue'] * df_single_stock['CO2Emissions/EnergyUse']
df_single_stock['CEIScope123'] = df_single_stock['Revenue/Employee'] * df_single_stock['EnergyUse/Revenue'] * df_single_stock['CO2Scope123/EnergyUse']

# Suppression des colonnes inutiles
df_single_stock.drop(columns=['Revenue/Employee', 'EnergyUse/Revenue', 'EnergyUse','CO2Scope12/EnergyUse','CO2Scope123/EnergyUse','CEIScope12','CEIScope123', 'CO2Emissions/EnergyUse' ], inplace=True)

# Création de la figure Plotly avec ajustement de la largeur des colonnes
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_single_stock.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_single_stock[col] for col in df_single_stock.columns],
               fill_color='lavender',
               align='left'))])

# Ajustement de la largeur des colonnes
column_widths = [1000] * len(df_single_stock.columns)  # Définir la largeur de chaque colonne ici (en pixels)
fig.update_layout(autosize=False, width=2200, height=600)  # Définir la taille de la figure
fig.update_layout({'xaxis': {'fixedrange': True}})  # Fixer la largeur de la table

# Affichage de la figure
fig.show()
