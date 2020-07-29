# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px

# Multi-dropdown options
from controls import COUNTRIES, METRIC_TYPES, COLORS

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Load data
df = pd.read_csv(DATA_PATH.joinpath("owid-covid-data.csv"), low_memory=False)
df["date"] = pd.to_datetime(df["date"])
df = df[df["date"] >= dt.datetime(2019, 12, 1)]

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport",
    "content": "width=device-width, initial-scale=1"}]
)

#app.config['suppress_callback_exceptions']=True
server = app.server

# Create controls
country_options = [
    {"label": str(COUNTRIES[country]), "value": str(country)} for country in COUNTRIES
]

metric_type_options = [
    {"label": str(METRIC_TYPES[metric_type]), "value": str(metric_type)}
    for metric_type in METRIC_TYPES
]

START_DATE = pd.to_datetime(df['date'].min())
END_DATE = pd.to_datetime(df['date'].max())
list_dts = pd.date_range( \
    START_DATE, END_DATE, freq='1d').tolist()



# Helper functions
epoch = dt.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() #* 1000.0

def get_marks(list_dates):

    dates = {}
    for i in range(len(list_dates)):
        dates[i] = {}
        dates[i] = list_dates[i]

    return dates

#slider_marks = get_marks(list_dts)
#print(slider_marks)

def filter_dataframe(df, metric_types, country_selected, date_slider):

    map_dates = get_marks(list_dts)

    #print(country_selected)
    dff = df[
        df["location"].isin([COUNTRIES[country_selected]])
        & (pd.to_datetime(df["date"]) >= map_dates[date_slider[0]])
        & (pd.to_datetime(df["date"]) <= map_dates[date_slider[1]])
    ]
    return dff

# Create global chart template
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"

layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)

#test_png = 'covid19-banner-3w.png'
#test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')


# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(  # Start of title row
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("mask.jpg"),
                            id="plotly-image",
                            style={
                                "height": "90px",
                                "width": "auto",
                                "margin-bottom": "10px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "COVID-19 Dashboard",
                                    style={"margin-bottom": "0px"},
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Coronavirus Source Data", id="learn-more-button"),
                            href="https://ourworldindata.org/coronavirus-source-data",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ), # End of title row
        html.Div( # start of first row of control panal + main plot
            [

                html.Div( # Start of control panel top left side
                    [
                        html.H5("Control Panel"),

                        html.Br(),
                        html.P(
                            "Filter by date (or select range in histogram):",
                            className="control_label",
                        ),
                        html.Br(),
                        dcc.RangeSlider(
                            id="date_slider",
                            min=0,
                            max=len(list_dts) - 1,
                            #step=1,
                            value=[0, len(list_dts) - 1],
                            #marks=slider_marks,
                            className="dcc_control",
                        ),

                        html.Br(),

                        html.P("Filter by metric type:", className="control_label"),
                        html.Br(),
                        dcc.RadioItems(
                            id="metric_type_selector",
                            options=[
                                {"label": "New Cases", "value": "new_cases"},
                                {"label": "New Deaths ", "value": "new_deaths"},
                                {"label": "Total Cases", "value": "total_cases"},
                                {"label": "Total Deaths ", "value": "total_deaths"},
                            ],
                            value="new_cases",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),

                        html.Br(),

                        html.P("Filter by country:", className="control_label"),
                        html.Br(),
                        dcc.Dropdown(
                            id="country_selected",
                            options=country_options,
                            multi=False,
                            value='210',
                            className="dcc_control",
                        ),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ), # End of control panel top left side

                html.Div( # Start of main plot top right side
                    [
                    dbc.Row(
                        html.Div(
                            [
                                #html.Div(
                                #    [html.P(id="summary"),],
                                #    id="Summary_container",
                                #    className="summary_mini_container",
                                #),
                                html.Div(
                                    [html.H6(id="totalCases"), html.P("Total Cases")],
                                    id="tc",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="totalDeaths"), html.P("Total Deaths")],
                                    id="td",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="newCases"), html.P("New Cases")],
                                    id="nc",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="newDeaths"), html.P("New Deaths")],
                                    id="nd",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        ),
                        html.Div(
                            [dcc.Graph(id="count_graph", config = {'displayModeBar' : False})],
                            id="countGraphContainer",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ), # End of main plot top right side
            ],
            className="row flex-display",
        ), # end of first row of control panal + main plot
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="main_graph")],
                    className="pretty_container fifteen columns",
                ),
            ],
            className="row flex-display",
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)


# Create callbacks
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("count_graph", "figure")],
)


@app.callback(
    Output("aggregate_data", "data"),
    [
        Input("metric_type_selector", "value"),
        Input("country_selected", "value"),
        Input("date_slider", "value"),
    ])
def update_text(metric_types, country_selected, date_slider):

    map_dates = get_marks(list_dts)
    data = filter_dataframe(df, metric_types, country_selected, date_slider)

    location = data['location'].values[-1].upper()
    dates = map_dates[date_slider[0]].strftime("%Y-%m-%d") + \
            " - " + map_dates[date_slider[1]].strftime("%Y-%m-%d")
    total_cases = data['total_cases'].values[-1]
    total_deaths = data['total_deaths'].values[-1]
    new_cases = data['new_cases'].values[-1]
    new_deaths = data['new_deaths'].values[-1]

    return [ \
            "{:,d}".format(int(total_cases)), \
            "{:,d}".format(int(total_deaths)), \
            "{:,d}".format(int(new_cases)), \
            "{:,d}".format(int(new_deaths))]


@app.callback(
    [
        Output("totalCases", "children"),
        Output("totalDeaths", "children"),
        Output("newCases", "children"),
        Output("newDeaths", "children"),
    ],
    [Input("aggregate_data", "data")],
)
def update_text(data):
    return data[0], data[1], data[2], data[3]


# Selectors -> count graph
@app.callback(
    Output("count_graph", "figure"),
    [
        Input("metric_type_selector", "value"),
        Input("country_selected", "value"),
        Input("date_slider", "value"),
    ],
)
def make_count_figure(metric_types, country_selected, date_slider):

    layout_count = copy.deepcopy(layout)

    data = filter_dataframe(df, metric_types, country_selected, date_slider)

    colors = []
    for i in range(len(list_dts)):
        if i >= int(date_slider[0]) and i <= int(date_slider[1]):
            colors.append("rgb(123, 199, 255)")
        else:
            colors.append("#FA9FB5")

    data = [
        dict(
            type="scatter",
            mode="markers",
            x=data['date'],
            y=data[metric_types],
            name=metric_types,
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="bar",
            x=data['date'],
            y=data[metric_types],
            name=metric_types,
            marker=dict(color=colors),
        ),
    ]

    layout_count["title"] = COUNTRIES[country_selected] + ": " + \
                        {v:k for k, v in METRIC_TYPES.items()}[metric_types]
    layout_count["dragmode"] = "select"
    layout_count["showlegend"] = False
    layout_count["autosize"] = True

    figure = dict(data=data, layout=layout_count)
    return figure


# Selectors -> main graph
@app.callback(
    Output("main_graph", "figure"),
    [
        Input("metric_type_selector", "value"),
    ],
)
def make_main_figure(metric_types):

    #data = filter_dataframe(df, metric_types, country_selected, date_slider)

    last_day = df['date'].max()
    sdf = df[(df['date']==last_day) & (~df['continent'].isnull())]
    sdf.fillna(0, inplace=True)

    #df = px.data.gapminder().query("year==2007")
    fig = px.scatter_geo(sdf,
                    locations="iso_code",
                    color="continent",
                    hover_name="location",
                    size="total_cases",
                    opacity=0.7,
                    title="Total cases by countries",
                    projection="robinson",
                    )
    return fig

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
