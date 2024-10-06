# NVIDIA Course
# Accelerating Data Engineering Pipelines 
from time import time


import cudf
import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import dask_cudf
from jupyter_dash import JupyterDash
import numpy as np
import pandas as pd
import plotly.graph_objects as go

verbose = True

# ---- Read Data ----
start_time = time()
if verbose:
    print("Loading data...")

# TODO: Update to read all CSVs
df = dask_cudf.read_csv(
    "data/*.csv",
    usecols=[ "STATION", "LATITUDE", "LONGITUDE", "DlySum", "DATE" ],
    dtype={
        "STATION": "object",
        "LATITUDE": np.float32,
        "LONGITUDE": np.float32,
        "DlySum": np.uint32,
        "DATE": str,
    },
    na_values=[ '-9999' ]
)

df = df.dropna()
if verbose:
    print(df.head())

# Define columns
seconds_elapsed = time() - start_time
if verbose:
    print(seconds_elapsed, "seconds")
start_time = time()
if verbose:
    print("Data loaded. Defining columns...")
df[ "Inches" ] = df[ "DlySum" ] / 100
df[ "TEXT" ] = df[ "STATION" ] + " - " + df[ "Inches" ].astype(str) + " inches"
df = df.compute()
# Set index for faster querying
date_min = df[ "DATE" ].min()
date_max = df[ "DATE" ].max()
df = df.set_index("DATE")

# Calculate color across all dataframes each day has same max
df[ "COLOR" ] = np.log10(df[ "Inches" ] + 1)
cmax = df[ "COLOR" ].max()

print(df.describe())

# df = df.to_pandas() # TODO: Delete this, and add one to each figure method

# ---- Define Dash App ----
seconds_elapsed = time() - start_time
if verbose:
    print(seconds_elapsed, "seconds")
start_time = time()
if verbose:
    print("Data computed. Defining Dash App...")

bgcolor = "rgb(25, 26, 26)"
ftcolor = "rgb(200, 200, 200)"
paper_bgcolor = "rgb(52, 51, 50)"
subunitcolor = "rgb(73, 73, 73)"

initial_date = date(2021, 1, 1)

app = JupyterDash(name)
server = app.server

app.layout = html.Div(
    [
        html.Div(
            [
                html.Span(
                    [
                        dcc.DatePickerSingle(
                            id="my-date-picker-single",
                            min_date_allowed=date_min,
                            max_date_allowed=date_max,
                            initial_visible_month=initial_date,
                            date=initial_date,
                        ),
                        daq.BooleanSwitch(
                            id="show-zeros",
                            on=True,
                            label="Show Zeros",
                            labelPosition="bottom",
                            style={"margin": "auto"},
                        ),
                    ],
                    style={
                        "width": "132px",
                        "display": "flex",
                        "flex-direction": "column",
                    },
                ),
                dcc.Markdown(
                    """
            # USA Precipitation Dashboard
            Welcome to the Preciptiation Dashboard based on NOAA's Hourly Precipitation Data.
            * Click a station on the map below to see its precipitation history from 1940 to 2020.
            * Click the date in the top left in order to change it. This can similarly be done by clicking a day
            on the time series below.
            * There are many days without any preciptiation. Click the toggle on the left to remove them from
            the map.
            """,
                    style={"padding": "0 35px 20px 20px"},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        dcc.Graph(
            id="precipitation-map",
            config={"modeBarButtonsToRemove": [ "select2d", "lasso2d" ]},
        ),
        dcc.Graph(id="time-series"),
    ],
    style={"color": ftcolor, "background-color": paper_bgcolor},
)

# ---- Define Callbacks ----
seconds_elapsed = time() - start_time
if verbose:
    print(seconds_elapsed, "seconds")
start_time = time()
if verbose:
    print("App defined. Creating Callbacks...")

plot_height = 250
plot_margin = {"r": 50, "t": 37