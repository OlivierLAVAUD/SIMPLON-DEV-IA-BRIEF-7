import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from api_client import get
from dash_req import *

racine_api = 'http://127.0.0.1:8000'

app = dash.Dash(__name__)

# Liste des feuilles de style externes
external_stylesheets = ['assets/style_voltaire.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Dashboard Agent"),

    html.Div([
        html.Label("Revenu Fiscal Moyen"),
        dcc.Input(id='input-revenu-year', type='text', value='2022'),
        dcc.Input(id='input-revenu-city', type='text', value='Paris'),
        html.Button('Valider', id='button-revenu'),
        html.Div(id='output-revenu'),
    ]),

    html.Div([
        html.Label("Transactions Sample"),
        dcc.Input(id='input-transactions-city', type='text', value='Paris'),
        html.Button('Valider', id='button-transactions'),
        html.Div(id='output-transactions'),
    ]),

    html.Div([
        html.Label("Acquisitions"),
        dcc.Input(id='input-acquisitions-city', type='text', value='Paris'),
        html.Button('Valider', id='button-acquisitions'),
        html.Div(id='output-acquisitions'),
    ]),

    html.Div([
        html.Label("Prix au mètre carré"),
        dcc.Input(id='input-prix-city', type='text', value='Paris'),
        html.Button('Valider', id='button-prix'),
        html.Div(id='output-prix'),
    ]),

    html.Div([
        html.Label("Nombre d'acquisitions"),
        dcc.Input(id='input-nombre-acquisitions-city', type='text', value='Paris'),
        html.Button('Valider', id='button-nombre-acquisitions'),
        html.Div(id='output-nombre-acquisitions'),
    ]),

    html.Div([
        html.Label("Count d'appartements par nombre de chambres"),
        dcc.Input(id='input-count-rooms-city', type='text', value='Paris'),
        html.Button('Valider', id='button-count-rooms'),
        html.Div(id='output-count-rooms'),
    ]),

    html.Div([
        html.Label("Moyenne du prix par mètre carré à Avignon"),
        html.Button('Valider', id='button-avg-prix-avignon'),
        html.Div(id='output-avg-prix-avignon'),
    ]),


])

# Callbacks
@app.callback(
    Output('output-revenu', 'children'),
    [Input('button-revenu', 'n_clicks')],
    [State('input-revenu-year', 'value'),
     State('input-revenu-city', 'value')]
)
def update_output_revenu(n_clicks, year, city):
    if n_clicks is not None:
        result = revenu_fiscal_moyen(year, city)
        return f"Revenu fiscal moyen: {result}"

@app.callback(
    Output('output-transactions', 'children'),
    [Input('button-transactions', 'n_clicks')],
    [State('input-transactions-city', 'value')]
)
def update_output_transactions(n_clicks, city):
    if n_clicks is not None:
        result = transactions_sample(city)
        return f"Transactions Sample: {result}"

@app.callback(
    Output('output-acquisitions', 'children'),
    [Input('button-acquisitions', 'n_clicks')],
    [State('input-acquisitions-city', 'value')]
)
def update_output_acquisitions(n_clicks, city):
    if n_clicks is not None:
        result = acquisitions(city)
        return f"Acquisitions: {result}"

@app.callback(
    Output('output-prix', 'children'),
    [Input('button-prix', 'n_clicks')],
    [State('input-prix-city', 'value')]
)
def update_output_prix(n_clicks, city):
    if n_clicks is not None:
        result = prix_au_metre_carre(city)
        return f"Prix au mètre carré: {result}"

@app.callback(
    Output('output-nombre-acquisitions', 'children'),
    [Input('button-nombre-acquisitions', 'n_clicks')],
    [State('input-nombre-acquisitions-city', 'value')]
)
def update_output_nombre_acquisitions(n_clicks, city):
    if n_clicks is not None:
        result = nombre_acquisitions(city)
        return f"Nombre d'acquisitions: {result}"

@app.callback(
    Output('output-count-rooms', 'children'),
    [Input('button-count-rooms', 'n_clicks')],
    [State('input-count-rooms-city', 'value')]
)
def update_output_count_rooms(n_clicks, city):
    if n_clicks is not None:
        result = count_appartments_rooms(city)
        return f"Count d'appartements par nombre de chambres: {result}"

@app.callback(
    Output('output-avg-prix-avignon', 'children'),
    [Input('button-avg-prix-avignon', 'n_clicks')]
)
def update_output_avg_prix_avignon(n_clicks):
    if n_clicks is not None:
        result = avg_prix_par_m2_avignon()
        return f"Moyenne du prix par mètre carré à Avignon: {result}"

@app.callback(
    Output('output-transactions-count-department', 'children'),
    [Input('button-transactions-count-department', 'n_clicks')],
    [State('input-transactions-count-department', 'value')]
)


if __name__ == '__main__':
    app.run_server(debug=True)
