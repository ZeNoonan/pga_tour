import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pathlib
import random
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

# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9548','canadian.csv')


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
memorial=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/memorial.csv','the memorial tournament presented by workday',2022)
canadian=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/canadian.csv','rbc canadian open',2022)


tournament_list=[masters,players, matchplay, riviera, bay_hill, scottsdale, kapalua, torrey_pines,innisbrook, jeddah, la_quinta,
dubai,hawaii,abu_dhabi,palm_beach,hilton_head, san_antonio, potomac,craig_ranch_texas,vidanta_mexico,pebble_beach, uspga,colonial,memorial,canadian]
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
overall_df=combined.copy()
overall_df['rolling_4_pts_count']=overall_df.groupby('Name')['Points Won'].rolling(4, min_periods=1).count().reset_index(0,drop=True).astype(int)
overall_df['rolling_4_pts_total']=overall_df.groupby('Name')['Points Won'].rolling(4, min_periods=1).sum().reset_index(0,drop=True)
overall_df['rolling_4_pts_mean']=overall_df.groupby('Name')['Points Won'].rolling(4, min_periods=1).mean().reset_index(0,drop=True)
overall_df['rolling_4_pts_median']=overall_df.groupby('Name')['Points Won'].rolling(4, min_periods=1).median().reset_index(0,drop=True)
overall_df['rolling_8_pts_count']=overall_df.groupby('Name')['Points Won'].rolling(8, min_periods=1).count().reset_index(0,drop=True).astype(int)
overall_df['rolling_8_pts_total']=overall_df.groupby('Name')['Points Won'].rolling(8, min_periods=1).sum().reset_index(0,drop=True)
overall_df['rolling_8_pts_mean']=overall_df.groupby('Name')['Points Won'].rolling(8, min_periods=1).mean().reset_index(0,drop=True)
overall_df['rolling_8_pts_median']=overall_df.groupby('Name')['Points Won'].rolling(8, min_periods=1).median().reset_index(0,drop=True)

week_number_1=st.number_input(label='select week number_1',min_value=2,key='week number',value=24)
number_of_events_1=int(st.number_input(label='number of events for points won',min_value=2,key='number weeks',value=8))
overall_df=overall_df[overall_df['Week']<(week_number_1+1)]
overall_df=overall_df[(overall_df['max_event']>(number_of_events_1-1))]
overall_df=overall_df.sort_values(['Name','Week'],ascending=True)
overall_df=overall_df.drop_duplicates(subset=['Name'], keep='last')

overall_df['med_4_rank']=overall_df['rolling_4_pts_median'].rank(method='dense', ascending=False)
overall_df['avg_4_rank']=overall_df['rolling_4_pts_mean'].rank(method='dense', ascending=False)
overall_df['med_8_rank']=overall_df['rolling_8_pts_median'].rank(method='dense', ascending=False)
overall_df['avg_8_rank']=overall_df['rolling_8_pts_mean'].rank(method='dense', ascending=False)
overall_df['avg_plus_med']=(overall_df['med_4_rank']+overall_df['avg_4_rank']+overall_df['med_8_rank']+overall_df['avg_8_rank'])
overall_df['avg_plus_med_rank']=overall_df['avg_plus_med'].rank(method='dense', ascending=True)
cols_to_move = ['Name','events_count','max_event','Week','Event Name','Pos','avg_plus_med_rank','avg_plus_med','med_4_rank','avg_4_rank','med_8_rank','avg_8_rank',
'rolling_8_pts_mean','rolling_8_pts_median']
cols = cols_to_move + [col for col in overall_df if col not in cols_to_move]
# selected_df=selected_df[cols].sort_values(by=['points_next_event'],ascending=False)
overall_df=overall_df[cols].sort_values(by='avg_plus_med_rank',ascending=True).reset_index(0,drop=True)

# combined=combined.sort_values(['Name','Week'],ascending=[True,False])
# selected_df=combined[combined['Week']<(week_number+1)].groupby('Name').head(number_of_events).reset_index(0,drop=True)
match_df=pd.read_excel('C:/Users/Darragh/Documents/Python/Golf/us_open.xlsx')
match_df=match_df.rename(columns={'Home':'Name'})
# st.write(match_df)
df_1=overall_df.loc[:,['Name','avg_plus_med_rank']]
df_2=pd.merge(match_df,df_1,on='Name')
df_1=df_1.rename(columns={'Name':'Away','avg_plus_med_rank':'rank_away'})
df_2=pd.merge(df_2,df_1,on='Away').rename(columns={'Name':'home','avg_plus_med_rank':'home_rank'})
df_2['diff']=df_2['home_rank']-df_2['rank_away']
df_2['abs']=df_2['diff'].abs()
df_2=df_2.sort_values(by='abs',ascending=False)
st.write(df_2.style.format(precision=0))


st.write(overall_df.style.format(precision=0))

# https://stackoverflow.com/questions/13996302/python-rolling-functions-for-groupby-object
# st.write(combined[combined['Name'].str.contains("Hovl")])

with st.expander('Last 8 events'):
    number_of_events=int(st.number_input(label='number of events for points won',min_value=2,key='number_weeks',value=8))
    week_number=st.number_input(label='select week number',min_value=2,key='week_number',value=20)
    combined=combined.sort_values(['Name','Week'],ascending=[True,False])
    selected_df=combined[combined['Week']<(week_number+1)].groupby('Name').head(number_of_events).reset_index(0,drop=True)
    selected_df=selected_df.sort_values(['Name','Week'],ascending=[True,True])

    # st.write('0',selected_df[selected_df['Name'].str.contains("Hovl")])
    selected_df=selected_df[(selected_df['max_event']>(number_of_events-1))]
    # st.write('1',selected_df[selected_df['Name'].str.contains("Hovl")])    
    # st.write('check out',selected_df.groupby('Name')['Points Won'])
    # selected_df['Points Won']=selected_df['Points Won'].replace(0,random.uniform(0,0.05))
    selected_df.loc[selected_df['Points Won'] == 0,'Points Won'] = selected_df['Points Won'].apply(lambda x: np.random.uniform(0,0.00005))
    # st.write('random',selected_df)
    # selected_df['rolling_pts_count']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).count().reset_index(0,drop=True).astype(int)
    selected_df['rolling_pts_count']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).count().reset_index(0,drop=True)
    selected_df['rolling_pts_total']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).sum().reset_index(0,drop=True)
    selected_df['rolling_pts_mean']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).mean().reset_index(0,drop=True).fillna(0)
    selected_df['rolling_pts_median']=selected_df.groupby('Name')['Points Won'].rolling(number_of_events, min_periods=number_of_events).median().reset_index(0,drop=True).fillna(0)

    # selected_df['avg_pts_rank']=selected_df['rolling_pts_mean'].rank(method='dense', ascending=False).astype(int)
    # selected_df['median_pts_rank']=selected_df['rolling_pts_median'].rank(method='dense', ascending=False).astype(int)
    # selected_df['avg_plus_med_rank']=(selected_df['avg_pts_rank']+selected_df['median_pts_rank']).rank(method='dense', ascending=True).astype(int)

    # st.write(selected_df[selected_df['Name'].str.contains("Hovl")])

    # first_step=combined[combined['Week']>(max(selected_df['Week']))].sort_values(['Name','Week'],ascending=True).drop_duplicates(subset=['Name'], keep='first')
    first_step=combined[combined['Week']==(week_number+1)].sort_values(['Name','Week'],ascending=True).drop_duplicates(subset=['Name'], keep='first')
    # st.write('first step', first_step)
    week_after_event=first_step.rename(columns={'Pos':'pos_next_event','Points Won':'points_next_event'})\
    .loc[:,['Name','pos_next_event','points_next_event']]
    # st.write(week_after_event)
    # st.write('check this for results', week_after_event)
    selected_df=pd.merge(selected_df,week_after_event,on='Name',how='right')
    # st.write('test this',selected_df[selected_df['Name'].str.contains("erger")])
    # selected_df['points_next_event']=selected_df['points_next_event'].fillna(0)

    selected_df['avg_pts_rank']=selected_df['rolling_pts_mean'].rank(method='dense', ascending=False)
    # selected_df['avg_pts_rank']=selected_df['rolling_pts_mean'].rank(method='dense', ascending=False).astype(int)
    selected_df['median_pts_rank']=selected_df['rolling_pts_median'].rank(method='dense', ascending=False)
    selected_df['avg_plus_med_rank']=(selected_df['avg_pts_rank']+selected_df['median_pts_rank']).rank(method='dense', ascending=True)
    
    player_names=selected_df['Name'].unique()
    names_selected = st.multiselect('Select Player',player_names)
    st.write((selected_df.set_index('Name').loc[names_selected,:]).reset_index().sort_values(by='Week',ascending=False).style.format(precision=0))

    selected_df=selected_df.sort_values(['Name','Week'],ascending=True)
    selected_df=selected_df.drop_duplicates(subset=['Name'], keep='last').sort_values(by='points_next_event',ascending=False).dropna(subset=['Week'])
    # selected_df['Week']=


    selected_df=selected_df.sort_values(by=['points_next_event'],ascending=False)
    selected_df['cum_median_rank']=selected_df['median_pts_rank'].cumsum()
    selected_df['cum_avg_rank']=selected_df['avg_pts_rank'].cumsum()
    selected_df['cum_avg_median_rank']=selected_df['avg_plus_med_rank'].cumsum()
    cols_to_move = ['Name','events_count','max_event','Week','Event Name','avg_pts_rank','median_pts_rank','avg_plus_med_rank','pos_next_event','points_next_event',
    'cum_median_rank','cum_avg_rank','cum_avg_median_rank','rolling_pts_median','rolling_pts_mean']
    cols = cols_to_move + [col for col in selected_df if col not in cols_to_move]
    # selected_df=selected_df[cols].sort_values(by=['points_next_event'],ascending=False)
    selected_df=selected_df[cols]


    # st.write(selected_df[selected_df['Name'].str.contains("Hovl")])
    # st.write(selected_df)
    list_of_events=combined.loc[:,['Week','Event Name','World Rating']].drop_duplicates().sort_values(by=['Week','World Rating'],ascending=[False,False]).reset_index(0,drop=True)
    list_of_events=list_of_events.groupby('Week').head(1)
    st.write(selected_df.set_index('Name').style.format(precision=0,formatter={('events_count','max_event','avg_pts_rank','median_pts_rank',
    'avg_plus_med_rank','points_next_event','cum_median_rank','cum_avg_rank','cum_avg_median_rank','Week'):"{:.2f}"}))
    st.write('Check this table against the golf rankings first version table')
    st.write(list_of_events)
    df_testing_ranking=selected_df.copy()
