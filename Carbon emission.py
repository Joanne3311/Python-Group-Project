#Importation of packages
import refinitiv.data.eikon as ek
from IPython.display import HTML
ek.set_app_key('a63d710c9a4f40efa8f37979cb8023d8c26966e4')
import refinitiv.data as rd
import numpy as np
import pandas as pd
import matplotlib as plt
%matplotlib inline
import warnings
import plotly.graph_objects as go
import pandas as pd
warnings.filterwarnings("ignore")


stock_symbol = 'SCHN.PA'  # Replace the value with another refinitiv stock acronym to get the datas for the stock wanted
# Datas retrieved for the studied stock
df_single_stock = rd.get_data(stock_symbol, ['TR.TRBCEconomicSector', 'TR.CO2EmissionTotal(Period=FY0)',
                              'TR.CO2IndirectScope3(Period=FY0)', 'TR.DividendYield','TR.EnvironmentPillarScore(Period=FY0)','TR.TRESGResourceUseScore(Period=FY0)', 
                              'TR.TRESGEmissionsScore(Period=FY0)','TR.TRESGInnovationScore(Period=FY0)', 'TR.EUTaxTotalEligibleAlignedRevenuePcent(Period=FY0)', 'TR.Tier1GreenRevenuePercentage(Period=FY0)','TR.Tier2GreenRevenuePercentage(Period=FY0)','TR.Tier3GreenRevenuePercentage(Period=FY0)'])

# Columns name
df_single_stock.columns = ['Instrument', 'Sector',  'CO2 Emissions Scope1&2', 'CO2 Emissions Scope3',
               'Dividend Yield','Environment Score', 'Resource Use Score', 'Emissions Score', 'Environmental Innovation Score', 'EU Taxonomy %Revenue Aligned', 'FTSE Tier 1 Green revenue', 'FTSE Tier 2 Green revenue', 'FTSE tier 3 Green revenue']

# Calculation of the CO2perYield ratio
df_single_stock['CO2 Per Yield'] = (df_single_stock['CO2 Emissions Scope1&2'] + df_single_stock['CO2 Emissions Scope3'])  / df_single_stock['Dividend Yield']
df_single_stock = df_single_stock.round(1)

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
fig.update_layout(autosize=False, width=1500, height=600)  # Height
fig.update_layout({'xaxis': {'fixedrange': True}})  # fix width


fig.show()
