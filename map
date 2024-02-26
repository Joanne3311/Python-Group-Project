#DataFrame, making us to input the stock symbols or company names

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
df = px.data.gapminder()

#Create the world map
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="country",
    hover_name="country",
    projection="natural earth",
)

app.layout = html.Div([
    dcc.Graph(figure=fig, id='world-map'),
    html.Label('Input the company name or stock symbols：'),
    dcc.Input(id='stock-input', type='text', value='AAPL'),
])


@app.callback(
    Output('world-map', 'figure'),
    Input('stock-input', 'value')
)
def update_map(selected_stock):
   
# Updating the map after inputting the specific name/stock code
    updated_fig = px.choropleth(
        df,
        locations="iso_alpha",
        color="country",
        hover_name="country",
        projection="natural earth",
    )

    return updated_fig


if __name__ == '__main__':
    app.run_server(debug=True)
