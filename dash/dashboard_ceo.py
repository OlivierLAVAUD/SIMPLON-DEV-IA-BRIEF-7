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
    html.H1("Dashboard CEO"),
    
 
    html.Div([
        html.Label("Transactions count par département"),
        dcc.Input(id='input-transactions-count-department', type='text', value='75'),
        html.Button('Valider', id='button-transactions-count-department'),
        html.Div(id='output-transactions-count-department'),
    ]),

    html.Div([
        html.Label("Vente d'appartements en 2022 avec foyer fiscal > 70k"),
        dcc.Input(id='input-vente-appart-city', type='text', value='Paris'),
        html.Button('Valider', id='button-vente-appart'),
        html.Div(id='output-vente-appart'),
    ]),

    html.Div([
        html.Label("Top 10 villes dynamiques"),
        html.Button('Valider', id='button-top-10-villes'),
        html.Div(id='output-top-10-villes'),
    ]),

    html.Div([
        html.Label("Top 10 prix plus bas par appartement"),
        html.Button('Valider', id='button-top-10-prix-bas'),
        html.Div(id='output-top-10-prix-bas'),
    ]),

    html.Div([
        html.Label("Top 10 prix plus haut par maison"),
        html.Button('Valider', id='button-top-10-prix-haut'),
        html.Div(id='output-top-10-prix-haut'),
    ]),
])

# Callbacks

@app.callback(
    Output('output-transactions-count-department', 'children'),
    [Input('button-transactions-count-department', 'n_clicks')],
    [State('input-transactions-count-department', 'value')]
)
def update_output_transactions_count_department(n_clicks, department):
    if n_clicks is not None:
        result = transactions_count_by_department(department)
        return f"Transactions count par département: {result}"

@app.callback(
    Output('output-vente-appart', 'children'),
    [Input('button-vente-appart', 'n_clicks')],
    [State('input-vente-appart-city', 'value')]
)
def update_output_vente_appart(n_clicks, city):
    if n_clicks is not None:
        result = vente_appart_2k22_foyer_70k(city)
        return f"Vente d'appartements en 2022 avec foyer fiscal > 70k: {result}"

@app.callback(
    Output('output-top-10-villes', 'children'),
    [Input('button-top-10-villes', 'n_clicks')]
)
def update_output_top_10_villes(n_clicks):
    if n_clicks is not None:
        result = top_10_ville_dynamic()
        return f"Top 10 villes dynamiques: {result}"

@app.callback(
    Output('output-top-10-prix-bas', 'children'),
    [Input('button-top-10-prix-bas', 'n_clicks')]
)
def update_output_top_10_prix_bas(n_clicks):
    if n_clicks is not None:
        result = top_10_prix_plus_bas_par_appart()
        return f"Top 10 prix plus bas par appartement: {result}"

@app.callback(
    Output('output-top-10-prix-haut', 'children'),
    [Input('button-top-10-prix-haut', 'n_clicks')]
)
def update_output_top_10_prix_haut(n_clicks):
    if n_clicks is not None:
        result = top_10_prix_plus_haut_par_maison()
        return f"Top 10 prix plus haut par maison: {result}"

if __name__ == '__main__':
    app.run_server(debug=True)
