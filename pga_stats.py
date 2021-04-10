import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

st.set_page_config(layout="wide")

# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest",
# }
# # https://stackoverflow.com/questions/64501788/api-web-data-capture
# url = "https://www.pgatour.com/content/pgatour/stats/stat.02674.y2021.eon.t536.html"
# # url = "https://www.pgatour.com/content/pgatour/stats/stat.02564.y2021.eon.t536.html"
# html = requests.get(url).text

# df = pd.read_html(html, flavor="html5lib")
# df = pd.concat(df).drop([0, 1, 2], axis=1)
# st.write(df.head())
# # df.to_csv("golf.csv", index=False)
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_536_masters.pkl')

riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_007_riviera_gc.pkl')
concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_473_wgc_concession.pkl')
bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_09_palmer_bay_hill.pkl')
sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_11_players_sawgrass.pkl')
honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_10_honda_classic.pkl')
san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_41_valero_texas.pkl')
masters=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_536_masters.pkl')

putt_riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_007_riviera_gc.pkl')
putt_concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_473_wgc_concession.pkl')
putt_bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_09_palmer_bay_hill.pkl')
putt_sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_11_players_sawgrass.pkl')
putt_honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_10_honda_classic.pkl')
putt_san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_41_valero_texas.pkl')
# putt_masters=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_536_masters.pkl')

st.write('masters', masters)

# st.write('masters', putt_masters.head())

def merge_golf(tee_to_green_stats,putting_stats, name_of_tournament,date):
    tee_to_green_stats = tee_to_green_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','SG:APR','SG:ARG','SG:OTT']].copy()
    putting_stats = putting_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','TOTAL SG:PUTTING']].copy()
    df = pd.merge(tee_to_green_stats, putting_stats, on=['PLAYER NAME', 'ROUNDS', 'MEASURED ROUNDS'])
    df['tournament']=name_of_tournament
    df['date']=date
    df=df.iloc[1:].copy()
    return df

riviera_stats=merge_golf(riviera, putt_riviera, 'riviera',1)
concession_stats=merge_golf(concession, putt_concession,'concession',2)
bay_hill_stats=merge_golf(bay_hill, putt_bay_hill,'bay_hill',3)
sawgrass_stats=merge_golf(sawgrass, putt_sawgrass,'sawgrass',4)
honda_stats=merge_golf(honda, putt_honda,'pga_national',5)
san_antonio_stats=merge_golf(san_antonio, putt_san_antonio,'tpc_san_antonio',6)

# st.write('riviera after clean', riviera_stats.head())

def clean_golf_tee(df):
    df['TOTAL SG:OTT']=df['SG:OTT']*df['MEASURED ROUNDS']
    df['TOTAL SG:APR']=df['SG:APR']*df['MEASURED ROUNDS']
    df['TOTAL SG:ARG']=df['SG:ARG']*df['MEASURED ROUNDS']
    col_list=['TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING']
    df['SG: TOTAL']=df[col_list].sum(axis=1)
    df['SG: TOTAL_AVG']=df['SG: TOTAL'] / df['MEASURED ROUNDS']
    df['Tee_Rank']= (df['TOTAL SG:OTT']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['Appr_Rank']=(df['TOTAL SG:APR']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['ARG_Rank']=(df['TOTAL SG:ARG']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['PUTT_Rank']=(df['TOTAL SG:PUTTING']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['SG_Rank']=(df['SG: TOTAL_AVG']).rank(method='dense', ascending=False)
    df['Rev_SG_Tot']=df['TOTAL SG:OTT']*0.28 + df['TOTAL SG:APR']*0.4 + df['TOTAL SG:ARG']*0.17 + df['TOTAL SG:PUTTING']*0.15
    df['Rev_SG_Rank']=(df['Rev_SG_Tot']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['Rev_Rank_Var'] = df['Rev_SG_Rank'] - df['SG_Rank']
    # df['Revised_Rev_SG_Tot']=df['TOTAL SG:OTT']*0.28 + df['TOTAL SG:APR']*0.4 + df['TOTAL SG:ARG']*0.17 + df['TOTAL SG:PUTT']*0.15
    rank_list=['Tee_Rank','Appr_Rank','ARG_Rank','PUTT_Rank']
    df['Rank_Equal']=df[rank_list].mean(axis=1).rank(method='dense', ascending=True)
    cols_to_move = ['PLAYER NAME','tournament','date','SG_Rank','TOTAL SG:OTT','Tee_Rank','TOTAL SG:APR','Appr_Rank','TOTAL SG:ARG','ARG_Rank','TOTAL SG:PUTTING','PUTT_Rank',
    'SG: TOTAL', 'SG: TOTAL_AVG','SG:OTT','SG:APR','SG:ARG','MEASURED ROUNDS','ROUNDS']
    cols = cols_to_move + [col for col in df if col not in cols_to_move]
    df=df[cols]
    df=df.reset_index().set_index('PLAYER NAME').drop(['index'],axis=1)
    df['ROUNDS']=df['ROUNDS'].astype(int)
    df['MEASURED ROUNDS']=df['MEASURED ROUNDS'].astype(int)
    df['SG_Rank']=df['SG_Rank'].astype(int)
    df['Appr_Rank']=df['Appr_Rank'].astype(int)
    df['ARG_Rank']=df['ARG_Rank'].astype(int)
    df['PUTT_Rank']=df['PUTT_Rank'].astype(int)
    df['Tee_Rank']=df['Tee_Rank'].astype(int)
    df['Rev_SG_Rank']=df['Rev_SG_Rank'].astype(int)
    df['Rev_Rank_Var']=df['Rev_Rank_Var'].astype(int)
    df['Rank_Equal']=df['Rank_Equal'].astype(int)
    # df=df.reset_index()
    return df.sort_values(by='SG: TOTAL_AVG', ascending=False)

riviera_stats = clean_golf_tee(riviera_stats)
concession_stats=clean_golf_tee(concession_stats)
bay_hill_stats=clean_golf_tee(bay_hill_stats)
sawgrass_stats=clean_golf_tee(sawgrass_stats)
pga_national_stats=clean_golf_tee(honda_stats)
san_antonio_stats=clean_golf_tee(san_antonio_stats)

# st.write('riviera after function', riviera_stats)

format_dict = {'TOTAL SG:OTT':'{0:,.1f}','SG:OTT':'{0:,.1f}', 'SG:APR':'{0:,.1f}' ,'TOTAL SG:APR':'{0:,.1f}' ,'TOTAL SG:ARG':'{0:,.1f}', 'SG:ARG':'{0:,.1f}', 
'SG:PUTT':'{0:,.1f}' , 'SG: TOTAL':'{0:,.1f}' , 'SG: TOTAL_AVG':'{0:,.1f}', 'Rev_SG_Tot':'{0:,.1f}', 'TOTAL SG:PUTTING':'{0:,.1f}','sg_rank':'{0:,.0f}',
'app_sg_rank':'{0:,.0f}','ott_rank':'{0:,.0f}','arg_rank':'{0:,.0f}','putt_rank':'{0:,.0f}','tee_to_green_rank':'{0:,.0f}','tee_green_rank':'{0:,.0f}'  }

combined = pd.concat([riviera_stats,concession_stats,bay_hill_stats,sawgrass_stats,pga_national_stats,san_antonio_stats])
combined = combined.reset_index()
st.write(combined.sort_values(by='SG: TOTAL_AVG',ascending=False).head().style.format(format_dict))



st.write('who has the best average approach the green rank?')
filtered = combined.groupby('PLAYER NAME').agg(total_rounds=('MEASURED ROUNDS','sum'),sg_rank=('SG_Rank','mean'),app_sg_rank=('Appr_Rank','mean'),
ott_rank=('Tee_Rank','mean'),arg_rank=('ARG_Rank','mean'),putt_rank=('PUTT_Rank','mean'))
rank_list=['app_sg_rank','ott_rank','arg_rank']
filtered['tee_to_green_rank']=filtered[rank_list].mean(axis=1).rank(method='dense', ascending=True)
filtered['tee_green_rank']=filtered['ott_rank']*0.28 + filtered['app_sg_rank']*0.4 + filtered['arg_rank']*0.17 
st.write('SG Rank',filtered.sort_values(by='sg_rank', ascending=True).query('`total_rounds`>4').style.format(format_dict))
st.write('Approach the Green [Irons] Rank',filtered.sort_values(by='app_sg_rank', ascending=True).query('`total_rounds`>4').style.format(format_dict))
st.write('Normalised Tee to Green Rank',filtered.sort_values(by='tee_green_rank', ascending=True).query('`total_rounds`>4').style.format(format_dict))
st.write('Equal amount for driving/irons/short game Tee to Green Rank',filtered.sort_values(by='tee_to_green_rank', ascending=True).query('`total_rounds`>4').style.format(format_dict))

st.write(combined[combined['PLAYER NAME'].str.contains('Collin')])









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
