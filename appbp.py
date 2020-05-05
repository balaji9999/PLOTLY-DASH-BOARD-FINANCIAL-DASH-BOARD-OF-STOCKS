# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:13:05 2020

@author: mange
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd


df=pd.read_csv("app_BP.csv",index_col="Date")
x=str(df.CLOSE[[-1]])+'GBX'
z=x[19:24]+"  "+ x[-3:]
y=df.index[[-1]]

df1=pd.read_csv("app_BP1.csv",index_col="Year")

df2=pd.read_csv("app_BP2.csv")


dff = pd.read_csv("mapbp.csv",index_col="index")








trace_line = go.Scatter(x=list(df.index),
                                y=list(df.CLOSE),
                               
                                name="Close",
                                showlegend=False)
trace_candle = go.Candlestick(x=df.index,
                           open=df.OPEN,
                           high=df.HIGH,
                           low=df.LOW,
                           close=df.CLOSE,
                           
                           visible=False,
                           showlegend=False)

trace_bar = go.Ohlc(x=df.index,
                           open=df.OPEN,
                           high=df.HIGH,
                           low=df.LOW,
                           close=df.CLOSE,
                           
                           visible=False,
                           showlegend=False)



close=df.CLOSE
smaclose=close.rolling(window=20).mean()
emaclose=close.ewm(span=20, adjust=False).mean()
trace_SMA = go.Scatter(x=list(df.index),
                                y=list(smaclose),
                                
                                name="SMA",
                                showlegend=False)

trace_EMA = go.Scatter(x=list(df.index),
                                y=list(emaclose),
                                
                                name="EMA",
                                showlegend=False)


trace_SELECT = go.Scatter(x=list(df.index),
                                y=list(),
                                
                                name="select",
                                showlegend=False)



values1=[df1.equity.iloc[4],df1.debt.iloc[4]]
values2=[df1.equity.iloc[3],df1.debt.iloc[3]]
values3=[df1.equity.iloc[2],df1.debt.iloc[2]]
values4=[df1.equity.iloc[1],df1.debt.iloc[1]]
values5=[df1.equity.iloc[0],df1.debt.iloc[0]]
labels2=['equity','debt']
trace_pie1=go.Pie(labels=labels2,values=values1)
trace_pie2=go.Pie(labels=labels2,values=values2)
trace_pie3=go.Pie(labels=labels2,values=values3)
trace_pie4=go.Pie(labels=labels2,values=values4)
trace_pie5=go.Pie(labels=labels2,values=values5)



values11=[df1.DOWNSTREAM.iloc[4],df1.UPSTREAM.iloc[4]]
values22=[df1.DOWNSTREAM.iloc[3],df1.UPSTREAM.iloc[3]]
values33=[df1.DOWNSTREAM.iloc[2],df1.UPSTREAM.iloc[2]]
values44=[df1.DOWNSTREAM.iloc[1],df1.UPSTREAM.iloc[1]]
values55=[df1.DOWNSTREAM.iloc[0],df1.UPSTREAM.iloc[0]]
labels22=['Downstream','Upstream']
trace_pie11=go.Pie(labels=labels22,values=values11)
trace_pie22=go.Pie(labels=labels22,values=values22)
trace_pie33=go.Pie(labels=labels22,values=values33)
trace_pie44=go.Pie(labels=labels22,values=values44)
trace_pie55=go.Pie(labels=labels22,values=values55)


updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Line',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False]}],
                    label='Candle',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True]}],
                    label='Bar',
                    method='update'
                ),
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),
                        
                        
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False,False]}],
                    label='SELECT',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False,True, False]}],
                    label='SMA',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False,False,True]}],
                    label='EMA',
                    method='update'
                ),
                        
                
                
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.3,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),    
    
    ])


updatemenus1 = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False,False, False]}],
                    label='2019',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False,False, False]}],
                    label='2018',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True,False, False]}],
                    label='2017',
                    method='update'
                ),
                        
                 dict(
                    args=[{'visible': [False, False, False,True,False]}],
                    label='2016',
                    method='update'
                ),       
                        
                dict(
                    args=[{'visible': [False, False, False,False, True]}],
                    label='2015',
                    method='update'
                ),    
                        
                        
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),
    ])



updatemenus11 = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False,False, False]}],
                    label='2019',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False,False, False]}],
                    label='2018',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True,False, False]}],
                    label='2017',
                    method='update'
                ),
                        
                 dict(
                    args=[{'visible': [False, False, False,True,False]}],
                    label='2016',
                    method='update'
                ),       
                        
                dict(
                    args=[{'visible': [False, False, False,False, True]}],
                    label='2015',
                    method='update'
                ),    
                        
                        
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),
                        
                    
        
    ])





data = [trace_line, trace_candle, trace_bar,trace_SELECT,trace_SMA, trace_EMA]

layout1=dict(title="STOCK CHART OF BP",showlegend=False,height=600,updatemenus=updatemenus)
fig=dict(data=data,layout=layout1)




data1 = [trace_pie1, trace_pie2,trace_pie3,trace_pie4,trace_pie5]
layout2=dict(title="DEBT & EQUITY BP",showlegend=True,updatemenus=updatemenus1)
fig1=dict(data=data1,layout=layout2)


data11 = [trace_pie11, trace_pie22,trace_pie33,trace_pie44,trace_pie55]
layout22=dict(title="DOWNSTREAM VS UPSTREAM",showlegend=True,updatemenus=updatemenus11)
fig11=dict(data=data11,layout=layout22)




std = close.rolling(window=20).std() 
upper = smaclose + (std * 2)
lower= smaclose - (std * 2)



external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


app = dash.Dash(__name__,external_stylesheets=external_stylesheets)


app.layout = html.Div([

                        html.Div([   
                                html.H1(children='BRITISH PETROLEUM DASH BOARD'),
                                html.Img(src="/assets/app_BP.png"),
                                ],className="banner"),

                        html.Div([
                                html.H2(children='BP : CURRENT STOCK PRICE:')
                                ]),
                        html.Div([
                                html.H3(z),
                                
                                ],style={'color': 'blue'}),


                        html.Div([
                            dcc.Graph(id="stock chart",figure=fig),
                                ]),

                        html.Div([
                             html.Div([
                                     dcc.Graph( id="BB",
                                          figure={
                                                   'data': [
                                                        {'x':list(df.index) ,'y': list(close) ,'type':'scatter','name':'CLOSE PRICE'},
                                                        {'x':list(df.index) ,'y': list(smaclose) ,'type':'scatter','name':'SMA'},
                                                        {'x':list(df.index) ,'y': list(upper) ,'type':'scatter','name':'UB'},
                                                        {'x':list(df.index) ,'y': list(lower) ,'type':'scatter','name':'LB'},
                                                        
                                                           ],
                                                   'layout':{
                                                           'title':'BollingerBands'
                                                           }
                                                   }
                                        )
                                ],className="six columns",style={'padding': 20}),

                         

                                  ],className="row"),

                       html.Div([
                                html.Div([
                                
                                    dcc.Graph(
                                            id='liquidity',
                                            figure={
                                                   'data': [
                                                        {'x':list(df1.index) ,'y': list(df1.TCA) ,'type':'bar','name':'TOTAL CURRENT ASSETS'},
                                                        {'x':list(df1.index) ,'y': list(df1.TCL) ,'type':'bar','name':'TOTAL CURRENT LIABILITIES'}
                                                           ],
                                                   'layout':{
                                                           'title':'TCA Vs TCL'
                                                           }
                                                   }
                                            )
                                        ],className="six columns",style={'padding': 20}),
                                html.Div([
                               
                                    dcc.Graph(
                                            id='liquidity1',
                                            figure={
                                                   'data': [
                                                        {'x':list(df1.index) ,'y': list(df1.CR) ,'type':'line','name':'CURRENT RATIO OF BP'},
                                                        {'x':list(df1.index) ,'y': list(df1.QR) ,'type':'line','name':'QUICK RATIO OF BP'},
                                                        {'x':list(df1.index) ,'y': list(df1.IACR) ,'type':'line','name':'IND Avg CR'},
                                                        {'x':list(df1.index) ,'y': list(df1.IAQR) ,'type':'line','name':'IND Avg QR'},
                                                           ],
                                                   'layout':{
                                                           'title':'QR & CR'
                                                           }
                                                   }
                                            )
                    
                                        ],className="six columns",style={'padding': 20})
                            
                               ],className="row"),


                        html.Div([
                                 html.Div([
                               
                                    dcc.Graph(
                                        id='AMR',
                                        figure={
                                               'data': [
                                                    {'x':list(df1.index) ,'y': list(df1.ITR) ,'type':'line','name':'Inventory turnover ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.IAITR) ,'type':'line','name':'Ind Avg Inventory TR'},
                                                    {'x':list(df1.index) ,'y': list(df1.FATR) ,'type':'line','name':'Fixed Asset TR'},
                                                    {'x':list(df1.index) ,'y': list(df1.IAFATR) ,'type':'line','name':'Ind Avg Fixed Asset TR'}
                                                       ],
                                               'layout':{
                                                       'title':'Inventory TR & Fixed Asset TR '
                                                       }
                                                   }
                                               )
                                        ],className="six columns",style={'padding': 20}),
                                html.Div([
                                
                                    dcc.Graph(
                                        id='DMR',
                                        figure={
                                               'data': [
                                                    {'x':list(df1.index) ,'y': list(df1.D_ER) ,'type':'line','name':'Debt/Equity ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.IAD_ER) ,'type':'line','name':'Ind Avg D/E Ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.TIE) ,'type':'line','name':'TIE Ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.IATIE) ,'type':'line','name':'Ind Avg TIE Ratio'}                                
                                                    
                                                       ],
                                               'layout':{
                                                       'title':'D/E Ratio & TIE'
                                                       }
                                                   }
                                               )
                                        ],className="six columns",style={'padding': 20}),
                            
                               ],className="row"),
                        

                         html.Div([
                                  html.Div([
                              
                                    dcc.Graph(
                                        id='PR',
                                        figure={
                                               'data': [
                                                    {'x':list(df1.index) ,'y': list(df1.GPM) ,'type':'line','name':'GPM ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.IAGPM) ,'type':'line','name':'Ind Avg GPM Ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.OM) ,'type':'line','name':'OM Ratio'},
                                                    {'x':list(df1.index) ,'y': list(df1.IAOM) ,'type':'line','name':'Ind Avg OM Ratio'}
                                                       ],
                                               'layout':{
                                                       'title':'GPM & OM Ratio'
                                                       }
                                                   }
                                               )
                                        ],className="six columns",style={'padding': 20}),



                                 html.Div([       
                                            dcc.Graph(
                                                    id='PR2',
                                                    figure={
                                                           'data': [
                                                                {'x':list(df1.index) ,'y': list(df1.RTA) ,'type':'line','name':'RTA ratio'},
                                                                {'x':list(df1.index) ,'y': list(df1.IARTA) ,'type':'line','name':'Ind Avg RTA Ratio'},
                                                                {'x':list(df1.index) ,'y': list(df1.ROE) ,'type':'line','name':'ROE ratio'},
                                                                {'x':list(df1.index) ,'y': list(df1.IAROE) ,'type':'line','name':'Ind Avg ROE Ratio'}
                                                                   ],
                                                           'layout':{
                                                                   'title':'RTA & ROE  Ratio'
                                                                   }
                                                           }
                                                    )
                                                ],className="six columns",style={'padding': 20}),

            
                                       ],className="row"),
 

                       html.Div([
                            
                                html.Div([
                                    dash_table.DataTable(
                                            id='table',
                                            data=df2.to_dict('records'),
                                            columns=[{'name':i,'id':i} for i in df2.columns],
                                            fixed_columns={ 'headers': True, 'data': 1 },
                                            style_as_list_view=True,
                                            style_header={'backgroundColor':  '#008000','fontWeight': 'bold'},
                                                          style_cell={
                                                                  'backgroundColor': 'rgb(50, 50, 50)',
                                                                  'color': 'white',                           
                                                                  'height': 'auto',
                                                                  'font_family': 'Times New Roman',
                                                                  'font_size': '31.87px',
                                                                  'text_align': 'center'
                                        
                                                                      },
                
                                                            )                        
                                                                       
                                        ],className="six columns",style={'padding': 5}),
                
                            
                                html.Div([       
                                    dcc.Graph(
                                            id='revenuue',
                                            figure={
                                                   'data': [
                                                        {'x':list(df1.index) ,'y': list(df1.REVENUE) ,'type':'bar','name':'BP REVENUE'},
                                                        {'x':list(df1.index) ,'y': list(df1.NETINCOME) ,'type':'bar','name':'BP NET INCOME'}
                                                           ],
                                                   'layout':{
                                                           'title':'BP REVENUE Vs INCOME'
                                                           }
                                                   }
                                            )
                                        ],className="six columns",style={'padding': 20,}),

                                ],className="row"),

                     html.Div([
                              html.Div([
                                      dcc.Graph(id="debt & equity",figure=fig1)
                                      ],className="six columns",style={'padding': 20}),


                             html.Div([
                                      dcc.Graph(id="DOWNSTREAM_UPSTREAM",figure=fig11)
                                      ],className="six columns",style={'padding': 20}),

                                                
                          ],className="row")

                     ])
                         
if __name__ == '__main__':
    app.run_server(debug=True)
