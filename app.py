import json
from flask import Flask, render_template
import sqlite3
from matplotlib.pyplot import title
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("lumber.db")
    cur = conn.cursor()
    df = pd.read_sql_query("""SELECT * from LUMBER""", conn)
    conn.close()

    fig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['open'],
    mode='lines',)
    ])

    highFig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['high'],
    mode='lines',)
    ])

    lowFig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['low'],
    mode='lines',)
    ])

    closeFig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['close'],
    mode='lines',)
    ])

    adjFig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['adj_close'],
    mode='lines',)
    ])

    volFig = go.Figure(data=[go.Scatter(
    x = df['date'],
    y = df['volume'],
    mode='lines',)
    ])

    fig.update_layout(
        title_text = "Lumber Data Graphs"
    )

    updatemenus = [
        {'buttons' : [{
                    'method': 'restyle',
                    'label' : 'open',
                    'args' : [{'y': [dat.y for dat in fig.data] }]
                    },
                    {
                    'method': 'restyle',
                    'label' : 'high',
                    'args' : [{'y': [dat.y for dat in highFig.data] }] 
                    },
                    {
                    'method': 'restyle',
                    'label' : 'low',
                    'args' : [{'y': [dat.y for dat in lowFig.data] }]
                    }, 
                    {
                    'method': 'restyle',
                    'label' : 'close',
                    'args' : [{'y': [dat.y for dat in closeFig.data] }]
                    },
                    {
                    'method': 'restyle',
                    'label' : 'adj_close',
                    'args' : [{'y': [dat.y for dat in adjFig.data] }]
                    },
                    {
                    'method': 'restyle',
                    'label' : 'volume',
                    'args' : [{'y': [dat.y for dat in volFig.data] }]
                    }
                    ],
                    'direction' : 'down',
                    'showactive' : True,
                    }
    ]

    fig = fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     step="day",
                     stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
    )

    fig.update_layout(
        updatemenus = updatemenus
    )


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)




