import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import requests

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real Estate Price Prediction Dashboard"),

    html.Div([
        html.Label("Longitude"),
        dcc.Input(id='input-longitude', type='number', value=0),
        html.Label("Latitude"),
        dcc.Input(id='input-latitude', type='number', value=0),
        html.Button('Predict Prix M2', id='button-predict-prix-m2'),
        html.Div(id='output-predict-prix-m2'),
    ]),

    html.Div([
        html.Label("Number of Rooms"),
        dcc.Input(id='input-n-pieces', type='number', value=0),
        html.Label("Surface Habitable"),
        dcc.Input(id='input-surface-habitable', type='number', value=0),
        html.Label("Prix M2"),
        dcc.Input(id='input-prix-m2', type='number', value=0),
        html.Label("Code Postal"),
        dcc.Input(id='input-code-postal', type='number', value=0),
        html.Label("Longitude"),
        dcc.Input(id='input-longitude-two', type='number', value=0),
        html.Label("Latitude"),
        dcc.Input(id='input-latitude-two', type='number', value=0),
        html.Button('Predict Prix M2 Two', id='button-predict-prix-m2-two'),
        html.Div(id='output-predict-prix-m2-two'),
    ]),
])

# Callbacks
@app.callback(
    Output('output-predict-prix-m2', 'children'),
    [Input('button-predict-prix-m2', 'n_clicks')],
    [State('input-longitude', 'value'),
     State('input-latitude', 'value')]
)
def update_output_predict_prix_m2(n_clicks, longitude, latitude):
    if n_clicks is not None:
        response = requests.get(f'http://127.0.0.1:8000/prix_m2/?longitude={longitude}&latitude={latitude}')
        result = response.json().get('predicted_prix_m2')
        return f"Predicted Prix M2: {result}"

@app.callback(
    Output('output-predict-prix-m2-two', 'children'),
    [Input('button-predict-prix-m2-two', 'n_clicks')],
    [State('input-n-pieces', 'value'),
     State('input-surface-habitable', 'value'),
     State('input-prix-m2', 'value'),
     State('input-code-postal', 'value'),
     State('input-longitude-two', 'value'),
     State('input-latitude-two', 'value')]
)
def update_output_predict_prix_m2_two(n_clicks, n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude):
    if n_clicks is not None:
        response = requests.get(f'http://127.0.0.1:8000/prix_m2_two/?n_pieces={n_pieces}&surface_habitable={surface_habitable}&prix_m2={prix_m2}&code_postal={code_postal}&longitude={longitude}&latitude={latitude}')
        result = response.json().get('predicted_prix_m2')
        return f"Predicted Prix M2 Two: {result}"

if __name__ == '__main__':
    app.run_server(debug=True)
