import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

def read_ogwr(url_comp):
    table=pd.read_html(url_comp)
    return table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv')



def clean_results(file_location,name_of_tournament,year):
    df=pd.read_csv(file_location)
    df['tournament']=name_of_tournament
    df['year']=year
    df['position']=df['Pos'].str.extract('(\d+)')
    df['MC']=np.where(df['Pos']=='MC',1,0)
    df=df.drop('Unnamed: 0',axis=1)
    return df

def further_clean(df):
    df['Adj_Pos']=pd.to_numeric(df['Adj_Pos'],errors='coerce')
    df['Adj_Pos']=df['Adj_Pos'].fillna(df['Pos'])
    return df

# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9461')
# table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv')
results_ogwr=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv','masters',2022)
# st.write(results_ogwr['Adj_Pos'].dtype)
results_ogwr=results_ogwr.rename(columns={'Name':'PLAYER NAME'})
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Cameron Davis'), 'PLAYER NAME' ] = 'Cam Davis'
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Siwoo Kim'), 'PLAYER NAME' ] = 'Si Woo Kim'
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Kyoung-Hoon Lee'), 'PLAYER NAME' ] = 'K.H. Lee'
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Sunghoon Kang'), 'PLAYER NAME' ] = 'Sung Kang'
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Sebastian Munoz'), 'PLAYER NAME' ] = 'Sebastián Muñoz'
results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Benjamin Taylor'), 'PLAYER NAME' ] = 'Ben Taylor'
st.write(results_ogwr)


# events=pd.read_html('http://www.owgr.com/events')
# events[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events['World Rating']=pd.to_numeric(ranking_events['World Rating'],errors='coerce')
st.write('world ranking events')
st.write(ranking_events)