import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pathlib
from st_aggrid import AgGrid, GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

st.set_page_config(layout="wide")

current_week=20

def clean_results(file_location,name_of_tournament,year):
    df=pd.read_csv(file_location)
    df['Event Name']=name_of_tournament
    df['year']=int(year)
    df['position']=df['Pos'].str.extract('(\d+)')
    df['MC']=np.where(df['Pos']=='MC',1,0)
    df=df.drop(['Unnamed: 0',"R1","R2","R3","R4","Agg",'Ctry'],axis=1)
    # df["R1"]=pd.to_numeric(df["R1"],errors='coerce')
    return df

def clean_results_matchplay(file_location,name_of_tournament,year):
    df=pd.read_csv(file_location)
    df['Event Name']=name_of_tournament
    df['year']=int(year)
    df['position']=df['Pos'].str.extract('(\d+)')
    df['MC']=np.where(df['Pos']=='MC',1,0)
    df=df.drop(['Unnamed: 0',"Agg",'Ctry'],axis=1)
    # df["R1"]=pd.to_numeric(df["R1"],errors='coerce')
    return df

def ogwr_file_csv_save(url_comp,filename_ext):
    table=pd.read_html(url_comp)
    p=pathlib.Path.cwd().joinpath('golf','rankings_data')
    return table[0].to_csv(p.joinpath(filename_ext))

# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9522','colonial.csv')


masters=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv','masters tournament',2022)
players=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/players.csv','the players championship',2022)
matchplay=clean_results_matchplay('C:/Users/Darragh/Documents/Python/Golf/rankings_data/matchplay.csv','wgc - dell technologies match play',2022)
riviera=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/riviera.csv','the genesis invitational',2022)
bay_hill=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/bay_hill.csv','arnold palmer invitational presented by mastercard',2022)
scottsdale=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/scottsdale.csv','wm phoenix open',2022)
kapalua=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/kapalua.csv','sentry tournament of champions',2022)
torrey_pines=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/torrey_pines.csv','farmers insurance open',2022)
innisbrook=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/innisbrook.csv','valspar championship',2022)
jeddah=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/jeddah.csv','pif saudi international powered by softbank investment advisers',2022)
la_quinta=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/la_quinta.csv','the american express',2022)
dubai=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/dubai.csv','slync.io dubai desert classic',2022)
hawaii=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/hawaii.csv','sony open in hawaii',2022)
abu_dhabi=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/abu_dhabi.csv','abu dhabi hsbc championship',2022)
palm_beach=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/palm_beach.csv','the honda classic',2022)
hilton_head=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/hilton_head.csv','rbc heritage',2022)
san_antonio=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/san_antonio.csv','valero texas open',2022)
potomac=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/potomac.csv','wells fargo championship',2022)
craig_ranch_texas=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/craig_ranch.csv','at&t byron nelson',2022)
vidanta_mexico=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/vidanta_mexico.csv','mexico open at vidanta',2022)
pebble_beach=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/pebble_beach.csv','at&t pebble beach pro-am',2022)
uspga=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/uspga.csv','u.s. pga championship',2022)
colonial=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/colonial.csv','charles schwab challenge',2022)

tournament_list=[masters,players, matchplay, riviera, bay_hill, scottsdale, kapalua, torrey_pines,innisbrook, jeddah, la_quinta,
dubai,hawaii,abu_dhabi,palm_beach,hilton_head, san_antonio, potomac,craig_ranch_texas,vidanta_mexico,pebble_beach, uspga,colonial]
combined=pd.concat(tournament_list,axis=0)

# events=pd.read_html('http://www.owgr.com/events')
# events[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events['World Rating']=pd.to_numeric(ranking_events['World Rating'],errors='coerce')
ranking_events['Event Name']=ranking_events['Event Name'].str.lower()
clean_ranking_event=ranking_events.loc[:,["Week","Year","Event Name","Winner's Points","World Rating","Home Rating","SoF"]]
combined=pd.merge(combined,clean_ranking_event,on=["Event Name"],how='outer').reset_index().drop('index',axis=1)
combined['Name']=combined['Name'].astype(str)
combined=combined.sort_values(['Name','Week'],ascending=True)

combined['events_count']=combined.groupby(['Name'])['Points Won'].cumcount()+1
combined['max_event']=combined.groupby('Name')['events_count'].transform('max')
combined['rolling_4_pts_count']=combined.groupby('Name')['Points Won'].rolling(4, min_periods=1).count().reset_index(0,drop=True).astype(int)
combined['rolling_4_pts_total']=combined.groupby('Name')['Points Won'].rolling(4, min_periods=1).sum().reset_index(0,drop=True)
combined['rolling_4_pts_mean']=combined.groupby('Name')['Points Won'].rolling(4, min_periods=1).mean().reset_index(0,drop=True)
combined['rolling_4_pts_median']=combined.groupby('Name')['Points Won'].rolling(4, min_periods=1).median().reset_index(0,drop=True)
combined['rolling_8_pts_count']=combined.groupby('Name')['Points Won'].rolling(8, min_periods=1).count().reset_index(0,drop=True).astype(int)
combined['rolling_8_pts_total']=combined.groupby('Name')['Points Won'].rolling(8, min_periods=1).sum().reset_index(0,drop=True)
combined['rolling_8_pts_mean']=combined.groupby('Name')['Points Won'].rolling(8, min_periods=1).mean().reset_index(0,drop=True)
combined['rolling_8_pts_median']=combined.groupby('Name')['Points Won'].rolling(8, min_periods=1).median().reset_index(0,drop=True)


# https://stackoverflow.com/questions/13996302/python-rolling-functions-for-groupby-object
st.write(combined[combined['Name'].str.contains("Scheff")])

with st.expander('Last 8 events'):
    number_of_events=int(st.number_input(label='number of events for points won',min_value=2,key='number_weeks',value=8))
    week_number=st.number_input(label='select week number',min_value=2,key='week_number',value=20)
    selected_df=combined[combined['Week']<(week_number+1)].groupby('Name').head(number_of_events).reset_index(0,drop=True)
    
    st.write('check out',selected_df.groupby('Name')['Points Won'])

    selected_df['rolling_pts_count']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).count().reset_index(0,drop=True).astype(int)
    # selected_df['rolling_pts_count']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=1).count().reset_index(0,drop=True).astype(int)
    selected_df['rolling_pts_total']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=1).sum().reset_index(0,drop=True)
    selected_df['rolling_pts_mean']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=1).mean().reset_index(0,drop=True).fillna(0)
    selected_df['rolling_pts_median']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=1).median().reset_index(0,drop=True).fillna(0)

    selected_df['avg_pts_rank']=selected_df['rolling_pts_mean'].rank(method='dense', ascending=False).astype(int)
    selected_df['median_pts_rank']=selected_df['rolling_pts_median'].rank(method='dense', ascending=False).astype(int)
    selected_df['avg_plus_med_rank']=(selected_df['avg_pts_rank']+selected_df['median_pts_rank']).rank(method='dense', ascending=True).astype(int)

    st.write(selected_df[selected_df['Name'].str.contains("Scheff")])

    week_after_event=combined[combined['Week']>(max(selected_df['Week']))].rename(columns={'Pos':'pos_next_event','Points Won':'points_next_event'})\
    .loc[:,['Name','pos_next_event','points_next_event']]

    selected_df=pd.merge(selected_df,week_after_event,on='Name',how='left')

    st.write(selected_df[selected_df['Name'].str.contains("Scheff")])