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
import warnings
import plotly.graph_objects as go
import pandas as pd
warnings.filterwarnings("ignore")


# Datas for the studied stock
stock_symbol = 'HRMS.PA'  # Replace the value of stock_symbol to get the datas for the stock wanted
df_single_stock = rd.get_data(stock_symbol, ['TR.TRBCEconomicSector', 'TR.CO2EmissionTotal(Period=FY0)',
                              'TR.CO2IndirectScope3(Period=FY0)', 'TR.DividendYield'])

# Columns name
df_single_stock.columns = ['Instrument', 'Sector',  'CO2Emissions', 'CO2EmissionsScope3',
               'DividendYield']

# Calculations
df_single_stock['CO2PerYield'] = (df_single_stock['CO2Emissions'] + df_single_stock['CO2EmissionsScope3'])  / df_single_stock['DividendYield']
df_single_stock = df_single_stock.round(3)
# Plotly package
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_single_stock.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_single_stock[col] for col in df_single_stock.columns],
               fill_color='lavender',
               align='left'))])

# Width and Height adjusting
column_widths = [1000] * len(df_single_stock.columns)  # Width
fig.update_layout(autosize=False, width=1000, height=600)  # Height
fig.update_layout({'xaxis': {'fixedrange': True}})  # fix width


fig.show()
