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

def further_clean(df):
    df['Adj_Pos']=pd.to_numeric(df['Adj_Pos'],errors='coerce')
    df['Adj_Pos']=df['Adj_Pos'].fillna(df['Pos'])
    return df

ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9466','hilton_head.csv')
# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9394','dubai.csv')


# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9461')
# table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2022.csv')
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


tournament_list=[masters,players, matchplay, riviera, bay_hill, scottsdale, kapalua, torrey_pines,innisbrook, jeddah, la_quinta,
dubai,hawaii,abu_dhabi,palm_beach,hilton_head]
combined=pd.concat(tournament_list,axis=0)
# st.write('combined', combined)
# st.write('masters',masters)
# st.write('matchplay',matchplay)

# st.write('players',players)

# st.write('riviera',riviera)
# st.write('bay_hill',bay_hill)
# st.write('kapalua',kapalua)
# st.write('innisbrook',innisbrook)

# events=pd.read_html('http://www.owgr.com/events')
# events[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events['World Rating']=pd.to_numeric(ranking_events['World Rating'],errors='coerce')
ranking_events['Event Name']=ranking_events['Event Name'].str.lower()
clean_ranking_event=ranking_events.loc[:,["Week","Year","Event Name","Winner's Points","World Rating","Home Rating","SoF"]]
st.write(clean_ranking_event)
combined=pd.merge(combined,clean_ranking_event,on=["Event Name"],how='outer')
st.write('world ranking events')

# st.write('combined', combined)
format_dict = {'ranking_points_total':'{0:,.0f}'}



with st.expander('Filter Combined Analysis by week'):

    week_pick=18
    # week_selection=((combined.set_index('Week').loc[week_pick,:]).reset_index().style.format(format_dict))
    week_selection=combined[combined['Week']<week_pick].copy()

    def analysis_golf(combined):
        filtered = combined.groupby('Name').agg(ranking_points_total=('Points Won','sum'),tournaments_played=('Points Won','count'),
        avg_ranking_points=('Points Won','mean'))
        filtered['avg_ranking_points_Rank']=(filtered['avg_ranking_points']).rank(method='dense', ascending=False)
        filtered['avg_ranking_points_Rank']=filtered['avg_ranking_points_Rank'].astype(int)
        filtered=filtered[filtered['ranking_points_total']>0].copy()
        return filtered

    grouped_analysis=analysis_golf(week_selection).sort_values(by=['avg_ranking_points_Rank'])
    # st.write(grouped_analysis)
    # grouped_database_players = analysis(combined)
    # st.write('This database gives an idea of who performed best across different tournaments')
    min_tournaments_played = st.number_input('Min Number of rounds played',min_value=3,step=1)
    avg_ranking=grouped_analysis.copy()
    avg_ranking=avg_ranking[avg_ranking['tournaments_played']>min_tournaments_played].reset_index()
    avg_ranking.index = np.arange(1, len(avg_ranking)+1)
    st.write(avg_ranking)
    # st.write(grouped_analysis[grouped_analysis['tournaments_played']>min_tournaments_played])

