import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

st.set_page_config(layout="wide")

# url = "https://www.europeantour.com/european-tour/stats/2021/leaderboard/?stats=DRIVING&type=SG_OFF_THE_TEE"
# url="https://stats.europeantour.com/api/v2/seasons/2021/stats/strokes-gained-off-the-tee"
# html = requests.get(url).text
# df = pd.read_html(html, flavor="html5lib")
# # df = pd.read_html(url)
# st.write(df)



# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest",
# }
# # https://stackoverflow.com/questions/64501788/api-web-data-capture
# # url = "https://www.pgatour.com/content/pgatour/stats/stat.02674.y2021.eon.t524.html"
# # url = "https://www.pgatour.com/content/pgatour/stats/stat.02564.y2021.eon.t524.html"
# url = "https://www.pgatour.com/competition/2021/the-honda-classic/leaderboard.html"
# html = requests.get(url).text

# df = pd.read_html(html, flavor="html5lib")
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/test.pkl')
# st.write(df)
# df = pd.concat(df).drop([0, 1, 2], axis=1)
# st.write(df.head())
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_524_detroit.pkl')
# # df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_524_detroit.pkl')

# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=8026')
# table[0].to_pickle('C:/Users/Darragh/Documents/Python/Golf/results_riviera.pkl')
# def clean_results(file_location,name_of_tournament,date):
#     df=pd.read_pickle(file_location)
#     df['tournament']=name_of_tournament
#     df['date']=date
#     df['Adj_Pos']=df['Pos'].str.replace('T','')
#     df['Adj_Pos']=pd.to_numeric(df['Adj_Pos'],errors='coerce')
#     df['Adj_Pos']=df['Adj_Pos'].fillna(df['Pos'])
#     return df

combined_results=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/results_combined.pkl')
# st.write(combined_results[combined_results['tournament'].str.contains('antonio')])
combined_results=combined_results.rename(columns={'Name':'PLAYER NAME'})
# st.write(combined_results.head())
combined_stats=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/combined_stats.pkl')
# st.write(combined_stats[combined_stats['tournament'].str.contains('antonio')])
# combined_stats['tournament']=combined_stats['tournament'].replace({'tpc_san_antonio':'san_antonio'})
# combined_stats.to_pickle('C:/Users/Darragh/Documents/Python/Golf/combined_stats.pkl')
# st.write(combined_stats[combined_stats['tournament'].str.contains('antonio')])
# st.write(combined.head())
combined = pd.merge(combined_stats, combined_results,on=['PLAYER NAME','tournament','date'],how='outer')
# st.write(test_combine.head())

# detroit=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_524_detroit.pkl')
# putt_detroit=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_524_detroit.pkl')

def merge_golf(tee_to_green_stats,putting_stats, name_of_tournament,date):
    tee_to_green_stats = tee_to_green_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','SG:APR','SG:ARG','SG:OTT']].copy()
    putting_stats = putting_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','TOTAL SG:PUTTING']].copy()
    df = pd.merge(tee_to_green_stats, putting_stats, on=['PLAYER NAME', 'ROUNDS', 'MEASURED ROUNDS'])
    df['tournament']=name_of_tournament
    df['date']=date
    df=df.iloc[1:].copy()
    return df

# detroit_stats=merge_golf(detroit, putt_detroit,'detroit',18)

def clean_golf_tee(df):
    df['TOTAL SG:OTT']=df['SG:OTT']*df['MEASURED ROUNDS']
    df['TOTAL SG:APR']=df['SG:APR']*df['MEASURED ROUNDS']
    df['TOTAL SG:ARG']=df['SG:ARG']*df['MEASURED ROUNDS']
    col_list=['TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING']
    df['SG: TOTAL']=df[col_list].sum(axis=1)
    sg_tee_to_green=['TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG']
    sg_tee_appr=['TOTAL SG:OTT','TOTAL SG:APR']
    df['TOTAL SG:TEE_ARG']=df[sg_tee_to_green].sum(axis=1)
    df['TOTAL SG:TEE_APR']=df[sg_tee_appr].sum(axis=1)
    df['SG: TOTAL_AVG']=df['SG: TOTAL'] / df['MEASURED ROUNDS']
    df['SG: Tee_Arg_AVG']=df['TOTAL SG:TEE_ARG'] / df['MEASURED ROUNDS']
    df['SG: Tee_App_AVG']=df['TOTAL SG:TEE_APR'] / df['MEASURED ROUNDS']
    df['Tee_Rank']= (df['TOTAL SG:OTT']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['Appr_Rank']=(df['TOTAL SG:APR']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['ARG_Rank']=(df['TOTAL SG:ARG']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['PUTT_Rank']=(df['TOTAL SG:PUTTING']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['SG_Rank']=(df['SG: TOTAL_AVG']).rank(method='dense', ascending=False)
    df['Tee_ARG_Rank']=(df['SG: Tee_Arg_AVG']).rank(method='dense', ascending=False)
    df['Tee_App_Rank']=(df['SG: Tee_App_AVG']).rank(method='dense', ascending=False)
    # df['Rev_SG_Tot']=df['TOTAL SG:OTT']*0.28 + df['TOTAL SG:APR']*0.4 + df['TOTAL SG:ARG']*0.17 + df['TOTAL SG:PUTTING']*0.15
    # df['Rev_SG_Rank']=(df['Rev_SG_Tot']/df['MEASURED ROUNDS']).rank(method='dense', ascending=False)
    df['Rev_Rank_Var'] = df['Tee_App_Rank'] - df['SG_Rank']
    # df['Revised_Rev_SG_Tot']=df['TOTAL SG:OTT']*0.28 + df['TOTAL SG:APR']*0.4 + df['TOTAL SG:ARG']*0.17 + df['TOTAL SG:PUTT']*0.15
    rank_list=['Tee_Rank','Appr_Rank','ARG_Rank','PUTT_Rank']
    # df['Rank_Equal']=df[rank_list].mean(axis=1).rank(method='dense', ascending=True)
    cols_to_move = ['PLAYER NAME','tournament','date','MEASURED ROUNDS','SG_Rank','SG: TOTAL','TOTAL SG:TEE_ARG','Tee_ARG_Rank','TOTAL SG:PUTTING','PUTT_Rank',
    'TOTAL SG:OTT','Tee_Rank','TOTAL SG:APR','Appr_Rank',
    'TOTAL SG:ARG','ARG_Rank',
    'SG: TOTAL_AVG','SG:OTT','SG:APR','SG:ARG','ROUNDS']
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
    df['Tee_ARG_Rank']=df['Tee_ARG_Rank'].astype(int)
    df['Tee_App_Rank']=df['Tee_App_Rank'].astype(int)
    df['Rev_Rank_Var']=df['Rev_Rank_Var'].astype(int)
    # df['Rank_Equal']=df['Rank_Equal'].astype(int)
    # df=df.reset_index()
    return df.sort_values(by='date', ascending=True)

# detroit_stats=clean_golf_tee(detroit_stats).reset_index()

format_dict = {'TOTAL SG:OTT':'{0:,.0f}','SG:OTT':'{0:,.0f}', 'SG:APR':'{0:,.0f}' ,'TOTAL SG:APR':'{0:,.0f}' ,'TOTAL SG:ARG':'{0:,.0f}', 'SG:ARG':'{0:,.0f}', 
'SG:PUTT':'{0:,.0f}' , 'SG: TOTAL':'{0:,.0f}' , 'SG: TOTAL_AVG':'{0:,.0f}', 'Rev_SG_Tot':'{0:,.1f}', 'TOTAL SG:PUTTING':'{0:,.0f}','sg_rank':'{0:,.0f}',
'app_sg_rank':'{0:,.0f}','ott_rank':'{0:,.0f}','arg_rank':'{0:,.0f}','normal_sg_no_putt':'{0:,.1f}','tee_green_normalised_sg':'{0:,.2f}',
'putt_rank':'{0:,.0f}','tee_to_green_rank':'{0:,.0f}','tee_green_rank':'{0:,.0f}','SG_Total':'{0:,.0f}','SG_Tee_Arg_Avg':'{0:,.1f}',
'SG_OTT':'{0:,.0f}','SG_APR':'{0:,.0f}','SG_ARG':'{0:,.0f}','SG_PUTT':'{0:,.0f}','SG_Total_Avg':'{0:,.1f}','Tee_Rank':'{0:,.0f}',
'SG_Total_Avg_Rank':'{0:,.0f}','SG_Tee_Arg':'{0:,.0f}','SG_OTT_Avg':'{0:,.1f}','SG_APR_Avg':'{0:,.1f}','SG_ARG_Avg':'{0:,.1f}','SG_PUTT_Avg':'{0:,.1f}',
'PUTT_Rank':'{0:,.0f}','SG_OTT_Avg_Rank':'{0:,.0f}','Tee_App_Rank':'{0:,.0f}','ARG_Rank':'{0:,.0f}','TOTAL SG:TEE:ARG':'{0:,.0f}','SG_Rank':'{0:,.0f}',
'SG :Tee_Arg_AVG':'{0:,.1f}','Tee_Arg_Rank':'{0:,.0f}','SG_Rank_less_Rank':'{0:,.0f}','TOTAL SG:TEE_APR':'{0:,.0f}','TOTAL SG:TEE_ARG':'{0:,.0f}','Appr_Rank':'{0:,.0f}'  }


# combined = pd.concat([combined,detroit_stats])
# combined = combined.reset_index()
# combined.to_pickle('C:/Users/Darragh/Documents/Python/Golf/stats_combined.pkl')


# st.write('this is combined database of the tournaments sorted by SG: TOTAL_AVG')
with st.beta_expander('Database sorted by Average Shots Gained from Tee to Putting for each Tournament'):
    st.write('This database gives an idea of who performed best across different tournaments')
    cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','Appr_Rank','Tee_Rank','ARG_Rank','PUTT_Rank','SG_Rank','Pos',
    'TOTAL SG:TEE_APR','TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING','SG: TOTAL',
    'SG: TOTAL_AVG','SG:OTT','SG:APR','SG:ARG','ROUNDS','MEASURED ROUNDS']
    cols = cols_to_move + [col for col in combined if col not in cols_to_move]
    combined=combined[cols]
    combined=combined.reset_index().drop('index',axis=1).sort_values(by='date',ascending=True)
    # st.write(combined.sort_values(by='SG: TOTAL_AVG',ascending=False).style.format(format_dict))
    
    st.write('Find a player')
    player_names=combined['PLAYER NAME'].unique()
    names_selected = st.multiselect('Select Player',player_names)
    st.write((combined.set_index('PLAYER NAME').loc[names_selected,:]).reset_index().style.format(format_dict))

    st.write('Find a tournament')
    tournament_name=combined['tournament'].unique()
    tournament_names = st.multiselect('Select Tournament',tournament_name)
    st.write((combined.set_index('tournament').loc[tournament_names,:]).set_index('PLAYER NAME').style.format(format_dict))

with st.beta_expander('Last Tournament Played'):
    last_tournament_played = combined.sort_values('date', ascending=False).drop_duplicates('PLAYER NAME').sort_values(by='SG: TOTAL_AVG',ascending=False)
    st.write('Last tournament played by Player')
    cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','Appr_Rank','Tee_Rank','PUTT_Rank','ARG_Rank','SG_Rank','Pos',
    'TOTAL SG:TEE_APR','TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING','SG: TOTAL',
    'SG:OTT','SG:APR','SG:ARG','ROUNDS','MEASURED ROUNDS']
    cols = cols_to_move + [col for col in last_tournament_played if col not in cols_to_move]
    last_tournament_played=last_tournament_played[cols]
    # st.write(last_tournament_played.style.format(format_dict))
    player_names_tour=last_tournament_played['PLAYER NAME'].unique()
    names_selected_tour = st.multiselect('Select Player',player_names_tour)
    st.write((last_tournament_played.set_index('PLAYER NAME').loc[names_selected_tour,:]).reset_index().style.format(format_dict))

def analysis(combined):
    filtered = combined.groupby('PLAYER NAME').agg(total_rounds=('MEASURED ROUNDS','sum'),SG_Total=('SG: TOTAL','sum'),SG_OTT=('TOTAL SG:OTT','sum'),
    SG_APR=('TOTAL SG:APR','sum'),SG_ARG=('TOTAL SG:ARG','sum'),SG_PUTT=('TOTAL SG:PUTTING','sum'))
    filtered['SG_Total_Avg'] = filtered['SG_Total'] / filtered['total_rounds']
    filtered['SG_Total_Avg_Rank']=(filtered['SG_Total_Avg']).rank(method='dense', ascending=False)
    tee_green_list =['SG_OTT', 'SG_APR','SG_ARG']
    sg_tee_appr=['SG_OTT', 'SG_APR']
    filtered['SG_Tee_Arg'] = filtered[tee_green_list].sum(axis=1)
    filtered['SG:Tee_Appr']=filtered[sg_tee_appr].sum(axis=1)
    # filtered['SG_Tee_Arg_Rank']=(filtered['SG_Tee_Arg']).rank(method='dense', ascending=False)
    filtered['SG_OTT_Avg'] = filtered['SG_OTT'] / filtered['total_rounds']
    filtered['Tee_Rank']=(filtered['SG_OTT_Avg']).rank(method='dense', ascending=False)
    filtered['SG_APR_Avg'] = filtered['SG_APR'] / filtered['total_rounds']
    filtered['Appr_Rank']=(filtered['SG_APR_Avg']).rank(method='dense', ascending=False)
    filtered['SG_ARG_Avg'] = filtered['SG_ARG'] / filtered['total_rounds']
    filtered['ARG_Rank']=(filtered['SG_ARG_Avg']).rank(method='dense', ascending=False)
    filtered['SG_PUTT_Avg'] = filtered['SG_PUTT'] / filtered['total_rounds']
    filtered['PUTT_Rank']=(filtered['SG_PUTT_Avg']).rank(method='dense', ascending=False)
    filtered['SG_Tee_Arg_Avg'] = filtered['SG_Tee_Arg'] / filtered['total_rounds']
    filtered['SG_Tee_Arg_Avg_Rank']=(filtered['SG_Tee_Arg_Avg']).rank(method='dense', ascending=False)
    filtered['SG_Tee_Appr_Avg'] = filtered['SG:Tee_Appr'] / filtered['total_rounds']
    filtered['Tee_App_Rank']=(filtered['SG_Tee_Appr_Avg']).rank(method='dense', ascending=False)

    filtered['SG_Rank_less_Rank'] = filtered['SG_Tee_Arg_Avg_Rank'] - filtered['SG_Total_Avg_Rank']
    cols_to_move = ['total_rounds','SG_Total_Avg_Rank','Tee_App_Rank','Appr_Rank','Tee_Rank','ARG_Rank','PUTT_Rank','SG_Tee_Arg_Avg','SG_Tee_Arg_Avg_Rank','SG_Rank_less_Rank','SG_PUTT_Avg',
    'SG_OTT_Avg','SG_APR_Avg','SG_ARG_Avg','SG_Total_Avg']
    cols = cols_to_move + [col for col in filtered if col not in cols_to_move]
    return filtered[cols]
    # return filtered


with st.beta_expander('Database grouped by Player over all tournaments'):
    grouped_database_players = analysis(combined)
    # st.write('This database gives an idea of who performed best across different tournaments')
    min_rounds_played = st.number_input('Min Number of rounds played',min_value=0,step=4)
    st.write(grouped_database_players[grouped_database_players['total_rounds']>min_rounds_played].sort_values(by='SG_Total_Avg',ascending=False).style.format(format_dict))
    # st.write(grouped_database_players.sort_values(by='SG_Total_Avg',ascending=False).style.format(format_dict))
    st.write('Find a player')
    grouped_database_players_index=grouped_database_players.reset_index()
    player_names_data=grouped_database_players_index['PLAYER NAME'].unique()
    names_selected_data = st.multiselect('Select Player',player_names_data)
    # st.write((grouped_database_players_index.set_index('PLAYER NAME').loc[names_selected_data,:]).style.format(format_dict))

