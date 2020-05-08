#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash


# In[2]:


import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# In[4]:


external_stylesheets = ['https://usfmumaanalyticsteam.github.io/learn.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('https://raw.githubusercontent.com/ritik777/data/master/tripadvisor_review.csv')


# In[5]:


df.head()


# In[ ]:


# for correlation between categories


# In[6]:


def generate_table(dataframe, max_rows=16):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# In[13]:


app.layout=html.Div([
    # Add your HTML tags to the content - notice a comma is added between HTML elements
    html.H1('tripadvisor_review_visualization'),
    html.Div([
        html.P('Category1 vs Category2'),
    ]),
    # Begin of DIV surrounding both Tables
    html.Div([
    # Begin of First Table
    html.Table(style={'width':'100%'},
               # Begin of Table children
               children=[
                   #######################################################################
                   # Begin of First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         
                         html.Th(style={'width':'30%'},
                             # Begin Th children
                             children=[
                                 html.H3('the graph')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Th
                         html.Th(style={'width':'70%'},
                             # Begin of Th children
                             children=[
                                 html.H3('correlation')
                             # End of Th children    
                             ]
                         
                         # End of Th
                         )
                         
                     # End of Tr children    
                     ]
                 # End of First Tr - Notice a comma is placed here to separate the next Tr
                 ),
                 #########################################################################
                 # Begin of Second Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Td
                         html.Td(
                             # Begin Td children
                             children=[
                                    # Display bar graph
                                    dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [
                                            {'x': df["Category 1"], 'y': df["Category 2"], 'type': 'line', 'name': 'correlation'},
                                        ],
                                        'layout': {
                                            'title': 'Correlation between category 1 and category 2'
                                        }
                                   }
                                # End of Chart 1
                                )
                              # End of Td children   
                             ]
                         ),


# In[15]:


if __name__ == '__main__':
    # Set debug to False. Some configurations are not setup for Debug
    app.run_server(debug=False)

