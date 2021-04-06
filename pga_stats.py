import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest",
# }

# url = "https://www.pgatour.com/content/pgatour/stats/stat.02564.y2021.eon.t041.html"
# html = requests.get(url).text

# df = pd.read_html(html, flavor="html5lib")
# df = pd.concat(df).drop([0, 1, 2], axis=1)
# st.write(df.head())
# # df.to_csv("golf.csv", index=False)
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_41_valero_texas.pkl')

riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_007_riviera_gc.pkl')
concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_473_wgc_concession.pkl')
bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_09_palmer_bay_hill.pkl')
sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_11_players_sawgrass.pkl')
honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_10_honda_classic.pkl')
san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_41_valero_texas.pkl')

putt_riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_007_riviera_gc.pkl')
putt_concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_473_wgc_concession.pkl')
putt_bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_09_palmer_bay_hill.pkl')
putt_sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_11_players_sawgrass.pkl')
putt_honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_10_honda_classic.pkl')
putt_san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_41_valero_texas.pkl')




st.write('riviera', riviera.head())
# st.write('concession', concession.head())
# st.write('bay_hill', bay_hill.head())
# st.write('sawgrass', sawgrass.head())
# st.write('honda', honda.head())
# st.write('san_antonio', san_antonio.head())

st.write('riviera', putt_riviera.head())
# st.write('concession', putt_concession.head())
# st.write('bay_hill', putt_bay_hill.head())
# st.write('sawgrass', putt_sawgrass.head())
# st.write('honda', putt_honda.head())
# st.write('san_antonio', putt_san_antonio.head())

def merge_golf(a,b):
    return pd.merge(a, b, on=['PLAYER NAME', 'ROUNDS', 'MEASURED ROUNDS'])

riviera_stats=merge_golf(riviera, putt_riviera)
concession_stats=merge_golf(concession, putt_concession)
bay_hill_stats=merge_golf(bay_hill, putt_bay_hill)
sawgrass_stats=merge_golf(sawgrass, putt_sawgrass)




def clean_golf_tee(df):
    df['SG:OTT']=df['SG:OTT']*df['MEASURED ROUNDS']
    df['SG:APR']=df['SG:APR']*df['MEASURED ROUNDS']
    df['SG:ARG']=df['SG:ARG']*df['MEASURED ROUNDS']
    col_list=['SG:OTT','SG:APR','SG:ARG','TOTAL SG:PUTTING']
    df['SG: TOTAL']=df[col_list].sum(axis=1)
    df['SG: TOTAL_AVG']=df['SG: TOTAL'] / df['MEASURED ROUNDS']
    df['Tee_Rank']= (df['SG:OTT']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['Appr_Rank']=(df['SG:APR']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['ARG_Rank']=(df['SG:ARG']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['PUTT_Rank']=(df['TOTAL SG:PUTTING']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['SG_Rank']=(df['SG: TOTAL_AVG']).rank(method='dense', ascending=False)
    rank_list=['Tee_Rank','Appr_Rank','ARG_Rank','PUTT_Rank']
    df['Rank_Rank']=df[rank_list].mean(axis=1).rank(method='dense', ascending=True)
    cols_to_move = ['PLAYER NAME','MEASURED ROUNDS','ROUNDS','SG:OTT','SG:APR','SG:ARG','TOTAL SG:PUTTING',
    'SG: TOTAL', 'SG: TOTAL_AVG', 'SG_Rank']
    cols = cols_to_move + [col for col in df if col not in cols_to_move]
    df=df[cols]
    st.write('1. Week 1 Pickle')
    st.table( df.sort_values(by='SG: TOTAL_AVG', ascending=False).head())



















# leaderboard_response = requests.get('https://lbdata.pgatour.com/2019/r/027/leaderboard.json').json()
# response =             requests.get('https://statdata.pgatour.com/r/006/2020/player_stats.json').json()
# # https://www.reddit.com/r/programmingrequests/comments/crizxq/seeking_help_with_pga_tour_web_scraping_project/

# players=pd.DataFrame(response['tournament']['players']).stats.apply(pd.Series)
# names=pd.DataFrame(response['tournament']['players']).pn.apply(pd.Series)
# sg_tee=pd.DataFrame(players.iloc[:,22].apply(pd.Series).loc[:,'tValue']).rename({'tValue':'sg_tee'}, axis=1)
# sg_iron=pd.DataFrame(players.iloc[:,21].apply(pd.Series).loc[:,'tValue']).rename({'tValue':'sg_iron'}, axis=1)
# sg_short=pd.DataFrame(players.iloc[:,20].apply(pd.Series).loc[:,'tValue']).rename({'tValue':'sg_short'}, axis=1)
# sg_putt=pd.DataFrame(players.iloc[:,19].apply(pd.Series).loc[:,'tValue']).rename({'tValue':'sg_putt'}, axis=1)
# sg_df=(pd.concat([names, sg_tee, sg_iron, sg_short, sg_putt], axis=1)).rename(columns={0:'player'})
# st.write(sg_df)

# st.write ( leaderboard_response)

# x=pd.DataFrame( players.iloc[:,22].apply(pd.Series).rounds.apply(pd.Series) )
# x=x.iloc[:,0].apply(pd.Series)
# # st.write (x)
