![Brief-7](Brief-7----.jpg "Brief-7")
# BRIEF 7
## Implémenter une interface interactive avec dash
# Dashboard Voltaire:  Agent & Ceo, Real Estate 

This is a dashboard application built using Dash, a Python framework for building analytical web applications. The dashboard provides insights related to various real estate metrics and financial data.

## Prerequisites

Make sure you have the following Python packages installed:

bash
```
`pip install dash` 
```
## Getting Started

1.  Clone the repository:

```
git clone <repository-url>
cd <repository-directory>` 
```
2.  Install the required packages:


```
`pip install -r requirements.txt` 
```
3.  Run the application:

```
`python ./dash/dashboard_Voltaire.py` 
```
4.  Open your web browser and navigate to [http://127.0.0.1:8050/](http://127.0.0.1:8050/) to view the dashboard.

# Voltaire Dashboard
## Dashboard Components: 

### Revenu Fiscal Moyen

-   Input fields for selecting the year and city.
-   Click the "Valider" button to calculate and display the Revenu Fiscal Moyen.

### Transactions Sample

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Transactions Sample.

### Acquisitions

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Acquisitions.

### Prix au mètre carré

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Prix au mètre carré.

### Nombre d'acquisitions

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Nombre d'acquisitions.

### Count d'appartements par nombre de chambres

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Count d'appartements par nombre de chambres.

### Moyenne du prix par mètre carré à Avignon

-   Click the "Valider" button to calculate and display the Moyenne du prix par mètre carré à Avignon.

### Transactions count par département

-   Input field for selecting the department.
-   Click the "Valider" button to calculate and display the Transactions count par département.

### Vente d'appartements en 2022 avec foyer fiscal > 70k

-   Input field for selecting the city.
-   Click the "Valider" button to calculate and display the Vente d'appartements en 2022 avec foyer fiscal > 70k.

### Top 10 villes dynamiques

-   Click the "Valider" button to calculate and display the Top 10 villes dynamiques.

### Top 10 prix plus bas par appartement

-   Click the "Valider" button to calculate and display the Top 10 prix plus bas par appartement.

### Top 10 prix plus haut par maison

-   Click the "Valider" button to calculate and display the Top 10 prix plus haut par maison.

Feel free to explore and interact with the different features of the dashboard to gain insights into real estate and financial data.

# Technical Aspects
api_client.py is a generic function to get information about endpoints using python package requests)
dash_req.py is a interface connector program used to decalare endpoints API functions for Dasboard
dashboard_voltaire is th gloabal dashboard use dash langage with callbacks

as required use

dashboard_agent.py

dashboard_ceo.py

dash_predict.py

dashboard_graph.py