import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import poliastro
from poliastro.plotting import OrbitPlotter3D
from poliastro.bodies import *
from poliastro.twobody.orbit import Orbit

def plot_object(objectplo):
	obj = Orbit.from_body_ephem(objectplo)
	a = OrbitPlotter3D()
	a.plot(orbit=obj, label=str(objectplo))
	return a.figure

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Poliastro - A Orbital Mechanics Visualisation tool'),
    html.Div(children='''
        Plot for earth around the sun:
    '''),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Earth', 'value': 'EAR'},
            {'label': 'Mars', 'value': 'MAR'},
            {'label': 'Jupiter', 'value': 'JUP'}
        ],
        value='NAN'
    ),

    dcc.Graph(
        id='Example Plot',
        figure= plot_object(Mars)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
