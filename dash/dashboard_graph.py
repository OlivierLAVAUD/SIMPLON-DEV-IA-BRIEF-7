import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash import dcc


# Charger le fichier CSV
df = pd.read_csv(r'data/transactions_upload.csv')

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Layout du tableau de bord
app.layout = html.Div([
    html.H1("Dashboard Transactions Sample"),

    # Graphique 1 : Histogramme du prix
    dcc.Graph(
        id='histogramme-prix',
        figure=px.histogram(df, x='prix', nbins=30, title='Histogramme du Prix')
    ),

    # Graphique 2 : Carte des transactions
    dcc.Graph(
        id='carte-transactions',
        figure=px.scatter_geo(
            df,
            lat='latitude',
            lon='longitude',
            color='prix',
            size='surface_habitable',
            hover_name='ville',
            title='Carte des Transactions'
        )
    ),

    # Graphique 3 : Boîte à moustaches (Box Plot) pour le nombre de pièces
    dcc.Graph(
        id='box-plot-n-pieces',
        figure=px.box(df, x='n_pieces', y='prix', points="all", title='Boîte à Moustaches - Nombre de Pièces')
    ),

    # Ajoutez d'autres graphiques selon vos besoins

])

# Exécutez l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
