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
# url = "https://www.pgatour.com/content/pgatour/stats/stat.02674.y2021.eon.t538.html"
# # url = "https://www.pgatour.com/content/pgatour/stats/stat.02564.y2021.eon.t538.html"
# html = requests.get(url).text

# df = pd.read_html(html, flavor="html5lib")
# df = pd.concat(df).drop([0, 1, 2], axis=1)
# # st.write(df.head())
# # df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_538_congaree.pkl')
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_538_congaree.pkl')

# table=pd.read_html('https://datagolf.com/live-tournament-stats')
# st.write(table[1])


riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_007_riviera_gc.pkl')
concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_473_wgc_concession.pkl')
bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_09_palmer_bay_hill.pkl')
sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_11_players_sawgrass.pkl')
honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_10_honda_classic.pkl')
san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_41_valero_texas.pkl')
# masters=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_536_masters.pkl')
harbour_town=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_012_harbour_town.pkl')
innisbrook=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_475_innisbrook.pkl')
quail_hollow=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_480_quail_hollow.pkl')
craig_ranch=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_019_craig_ranch.pkl')
kiawah_island=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_033_kiawah_island.pkl')
colonial=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_021_colonial.pkl')
memorial=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_023_memorial.pkl')
congaree=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_538_congaree.pkl')

putt_riviera=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_007_riviera_gc.pkl')
putt_concession=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_473_wgc_concession.pkl')
putt_bay_hill=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_09_palmer_bay_hill.pkl')
putt_sawgrass=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_11_players_sawgrass.pkl')
putt_honda=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_10_honda_classic.pkl')
putt_san_antonio=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_41_valero_texas.pkl')
# putt_masters=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_536_masters.pkl')
putt_harbour_town=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_012_harbour_town.pkl')
putt_innisbrook=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_475_innisbrook.pkl')
putt_quail_hollow=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_480_quail_hollow.pkl')
putt_craig_ranch=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_019_craig_ranch.pkl')
putt_kiawah_island=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_033_kiawah_island.pkl')
putt_colonial=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_021_colonial.pkl')
putt_memorial=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_023_memorial.pkl')
putt_congaree=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_538_congaree.pkl')

# st.write('harbour_town stats', harbour_town.head())

# st.write('harbour_town putt', putt_harbour_town.head())

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
harbour_town_stats=merge_golf(harbour_town, putt_harbour_town,'harbour_town',7)
innisbrook_stats=merge_golf(innisbrook, putt_innisbrook,'innisbrook',8)
quail_hollow_stats=merge_golf(quail_hollow, putt_quail_hollow,'quail_hollow',9)
craig_ranch_stats=merge_golf(craig_ranch, putt_craig_ranch,'craig_ranch',10)
kiawah_island_stats=merge_golf(kiawah_island, putt_kiawah_island,'kiawah_island',11)
colonial_stats=merge_golf(colonial, putt_colonial,'colonial',12)
memorial_stats=merge_golf(memorial, putt_memorial,'memorial',13)
congaree_stats=merge_golf(congaree, putt_congaree,'congaree',14)

# st.write('riviera after clean', riviera_stats.head())

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
    return df.sort_values(by='SG: TOTAL_AVG', ascending=False)

riviera_stats = clean_golf_tee(riviera_stats)
concession_stats=clean_golf_tee(concession_stats)
bay_hill_stats=clean_golf_tee(bay_hill_stats)
sawgrass_stats=clean_golf_tee(sawgrass_stats)
pga_national_stats=clean_golf_tee(honda_stats)
san_antonio_stats=clean_golf_tee(san_antonio_stats)
harbour_town_stats=clean_golf_tee(harbour_town_stats)
innisbrook_stats=clean_golf_tee(innisbrook_stats)
quail_hollow_stats=clean_golf_tee(quail_hollow_stats)
craig_ranch_stats=clean_golf_tee(craig_ranch_stats)
kiawah_island_stats=clean_golf_tee(kiawah_island_stats)
colonial_stats=clean_golf_tee(colonial_stats)
memorial_stats=clean_golf_tee(memorial_stats)
congaree_stats=clean_golf_tee(congaree_stats)

# st.write('riviera after function', riviera_stats)

format_dict = {'TOTAL SG:OTT':'{0:,.0f}','SG:OTT':'{0:,.0f}', 'SG:APR':'{0:,.0f}' ,'TOTAL SG:APR':'{0:,.0f}' ,'TOTAL SG:ARG':'{0:,.0f}', 'SG:ARG':'{0:,.0f}', 
'SG:PUTT':'{0:,.0f}' , 'SG: TOTAL':'{0:,.0f}' , 'SG: TOTAL_AVG':'{0:,.0f}', 'Rev_SG_Tot':'{0:,.1f}', 'TOTAL SG:PUTTING':'{0:,.0f}','sg_rank':'{0:,.0f}',
'app_sg_rank':'{0:,.0f}','ott_rank':'{0:,.0f}','arg_rank':'{0:,.0f}','normal_sg_no_putt':'{0:,.1f}','tee_green_normalised_sg':'{0:,.2f}',
'putt_rank':'{0:,.0f}','tee_to_green_rank':'{0:,.0f}','tee_green_rank':'{0:,.0f}','SG_Total':'{0:,.0f}','SG_Tee_Arg_Avg':'{0:,.1f}',
'SG_OTT':'{0:,.0f}','SG_APR':'{0:,.0f}','SG_ARG':'{0:,.0f}','SG_PUTT':'{0:,.0f}','SG_Total_Avg':'{0:,.1f}','Tee_Rank':'{0:,.0f}',
'SG_Total_Avg_Rank':'{0:,.0f}','SG_Tee_Arg':'{0:,.0f}','SG_OTT_Avg':'{0:,.1f}','SG_APR_Avg':'{0:,.1f}','SG_ARG_Avg':'{0:,.1f}','SG_PUTT_Avg':'{0:,.1f}',
'PUTT_Rank':'{0:,.0f}','SG_OTT_Avg_Rank':'{0:,.0f}','Tee_App_Rank':'{0:,.0f}','ARG_Rank':'{0:,.0f}','TOTAL SG:TEE:ARG':'{0:,.0f}',
'SG :Tee_Arg_AVG':'{0:,.1f}','Tee_Arg_Rank':'{0:,.0f}','SG_Rank_less_Rank':'{0:,.0f}','TOTAL SG:TEE_APR':'{0:,.0f}','TOTAL SG:TEE_ARG':'{0:,.0f}','Appr_Rank':'{0:,.0f}'  }

combined = pd.concat([riviera_stats,concession_stats,bay_hill_stats,sawgrass_stats,pga_national_stats,
san_antonio_stats,harbour_town_stats,innisbrook_stats,quail_hollow_stats,craig_ranch_stats,kiawah_island_stats,
colonial_stats,memorial_stats,congaree_stats])
# combined = pd.concat([riviera_stats,concession_stats,bay_hill_stats,sawgrass_stats,pga_national_stats,san_antonio_stats])
combined = combined.reset_index()

# st.write('this is combined database of the tournaments sorted by SG: TOTAL_AVG')
with st.beta_expander('Database sorted by Average Shots Gained from Tee to Putting for each Tournament'):
    st.write('This database gives an idea of who performed best across different tournaments')
    cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','Appr_Rank','Tee_Rank','ARG_Rank','PUTT_Rank','SG_Rank',
    'TOTAL SG:TEE_APR','TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING','SG: TOTAL',
    'SG: TOTAL_AVG','SG:OTT','SG:APR','SG:ARG','ROUNDS','MEASURED ROUNDS']
    cols = cols_to_move + [col for col in combined if col not in cols_to_move]
    combined=combined[cols]
    combined=combined.reset_index().drop('index',axis=1)
    st.write(combined.sort_values(by='SG: TOTAL_AVG',ascending=False).style.format(format_dict))
    
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
    cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','PUTT_Rank','Appr_Rank','Tee_Rank','ARG_Rank','SG_Rank',
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
    st.write((grouped_database_players_index.set_index('PLAYER NAME').loc[names_selected_data,:]).style.format(format_dict))

# with st.beta_expander('Find Player for Tournament Stats'):

    # st.write(combined[combined['PLAYER NAME'].str.contains('Lahiri')])
    # st.write('This database gives an idea of who performed best across different tournaments')


# st.write('who has the best average approach the green rank?')
# def update_analysis(combined):
#     filtered = combined.groupby('PLAYER NAME').agg(total_rounds=('MEASURED ROUNDS','sum'),sg_rank=('SG_Rank','mean'),app_sg_rank=('Appr_Rank','mean'),
#     ott_rank=('Tee_Rank','mean'),arg_rank=('ARG_Rank','mean'),putt_rank=('PUTT_Rank','mean'),normal_sg_no_putt=('Rev_SG_Tot','sum'))
#     rank_list=['app_sg_rank','ott_rank','arg_rank']
#     filtered['tee_to_green_rank']=filtered[rank_list].mean(axis=1).rank(method='dense', ascending=True)
#     filtered['tee_green_rank']=filtered['ott_rank']*0.28 + filtered['app_sg_rank']*0.4 + filtered['arg_rank']*0.17 
#     filtered['tee_green_normalised_sg'] = filtered['normal_sg_no_putt'] / filtered['total_rounds']
#     # filtered['tee_green_normalised_sg_rank'] = filtered['tee_green_normalised_sg'].rank(method='dense', ascending=True)
#     return filtered 

# filtered=update_analysis(combined)
# st.write('SG Rank',filtered.sort_values(by='sg_rank', ascending=True).query('`total_rounds`>4').style.format(format_dict))
# st.write('Approach the Green [Irons] Rank',filtered.sort_values(by='app_sg_rank', ascending=True).query('`total_rounds`>1').style.format(format_dict))
# st.write('Normalised Tee to Green Rank',filtered.sort_values(by='tee_green_rank', ascending=True).query('`total_rounds`>1').style.format(format_dict))
# st.write('Normalised Tee to Green Rank New Calc',filtered.sort_values(by='tee_green_normalised_sg', ascending=False).query('`total_rounds`>1').style.format(format_dict))
# st.write('Equal amount for driving/irons/short game Tee to Green Rank',filtered.sort_values(by='tee_to_green_rank', ascending=True).query('`total_rounds`>1').style.format(format_dict))

# st.write(combined[combined['PLAYER NAME'].str.contains('Si Woo')])

# Cross check against SG Average total here
# https://www.pgatour.com/stats/stat.02675.html

# st.write('overall stats')
# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02674.html')[1]).drop(['RANK LAST WEEK'], axis=1))
# st.write('test 1',a.head())
# b=pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02564.html')[1]).drop(['RANK LAST WEEK'], axis=1)
# st.write('test 2',b.head())
# df=pd.merge(a, b, on=['PLAYER NAME'], how='outer')    
# # df=df.drop(df.columns[[0,8,3,9]], axis=1)
# st.table(df.head(10))
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/stats_after_harbour_town_19April2021.pkl')

# with st.beta_expander('Run the above again in a day or two to see if Masters strokes gained is updated look at measured rounds'):
#     pass
    # full_stats_overall=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/stats_after_san_antonio_1.pkl')
    # st.write('after san antonio')
    # st.write(full_stats_overall.sort_values(by='SG:APR', ascending=False))
    # full_stats_overall=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/stats_after_masters.pkl')
    # st.write('after masters')
    # st.write(full_stats_overall.sort_values(by='SG:APR', ascending=False))
    # full_stats_overall=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_012_harbour_town.pkl')
    # st.write('harbour town')
    # st.write(full_stats_overall.sort_values(by='SG:APR', ascending=False))

# test=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/week_before_masters.pkl')
# st.write('test',test.sort_values(by='SG:APR', ascending=False))


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
