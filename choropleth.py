#import plotly and set notebook mode to True
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)


#import pandas and read the csv file
import pandas as pd
df = pd.read_csv('H:\Machine learning\API_ILO_country_YU.csv')


#create the data and layout dictionaries
data = dict(type='choropleth',
           locations=df['Country Name'],
           locationmode='country names',
           z=df['2014'],
           text=df['Country Name'],
           colorbar={'title':'2014'})
layout = dict(title='2014 Unemployment',
             geo=dict(showframe=False,projection={'type':'mercator'}))



#create the plot
choromap = go.Figure(data = [data], layout = layout)
iplot(choromap, validate=False)