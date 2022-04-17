import streamlit as st
import pandas as pd
import numpy as np
import pathlib

st.set_page_config(layout="wide")
# variable='masters.csv'
# p=pathlib.Path.cwd().joinpath('golf')
# st.write(p)


def read_ogwr(url_comp):
    table=pd.read_html(url_comp)
    return table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv')

def ogwr_file_csv_save(url_comp,filename_ext):
    table=pd.read_html(url_comp)
    p=pathlib.Path.cwd().joinpath('golf','rankings_data')
    return table[0].to_csv(p.joinpath(filename_ext))


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

# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9445','matchplay.csv')
# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9394','dubai.csv')


# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9461')
# table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv')
masters=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv','masters',2022)
players=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/players.csv','players',2022)
matchplay=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/matchplay.csv','matchplay',2022)
riviera=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/riviera.csv','riviera',2022)
bay_hill=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/bay_hill.csv','bay_hill',2022)
scottsdale=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/scottsdale.csv','scottsdale',2022)
kapalua=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/kapalua.csv','kapalua',2022)
torrey_pines=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/torrey_pines.csv','torrey_pines',2022)
innisbrook=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/innisbrook.csv','innisbrook',2022)
jeddah=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/jeddah.csv','jeddah',2022)
la_quinta=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/la_quinta.csv','la_quinta',2022)
dubai=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/dubai.csv','dubai',2022)

# st.write(results_ogwr['Adj_Pos'].dtype)
# results_ogwr=results_ogwr.rename(columns={'Name':'PLAYER NAME'})
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Cameron Davis'), 'PLAYER NAME' ] = 'Cam Davis'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Siwoo Kim'), 'PLAYER NAME' ] = 'Si Woo Kim'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Kyoung-Hoon Lee'), 'PLAYER NAME' ] = 'K.H. Lee'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Sunghoon Kang'), 'PLAYER NAME' ] = 'Sung Kang'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Sebastian Munoz'), 'PLAYER NAME' ] = 'Sebastián Muñoz'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Benjamin Taylor'), 'PLAYER NAME' ] = 'Ben Taylor'
st.write('masters',masters)
st.write('players',players)
st.write('matchplay',matchplay)
st.write('riviera',riviera)
st.write('bay_hill',bay_hill)
st.write('kapalua',kapalua)
st.write('innisbrook',innisbrook)

# events=pd.read_html('http://www.owgr.com/events')
# events[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events['World Rating']=pd.to_numeric(ranking_events['World Rating'],errors='coerce')
st.write('world ranking events')
st.write(ranking_events)