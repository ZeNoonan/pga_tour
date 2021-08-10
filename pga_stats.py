import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
import pickle

st.set_page_config(layout="wide")

combined=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/combined_1.pkl')




# combined_1=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/results_riviera.pkl')
# st.write('update',combined_1)

def clean_results(file_location,name_of_tournament,date):
    df=pd.read_pickle(file_location)
    # df=pd.read_html(file_location)
    # df=df[0].copy()
    df['tournament']=name_of_tournament
    df['date']=date
    df['Adj_Pos']=df['Pos'].str.replace('T','')
    df['Adj_Pos']=df['Pos'].str.replace('WD','')
    df['Adj_Pos']=pd.to_numeric(df['Adj_Pos'],errors='coerce')
    df['Adj_Pos']=df['Adj_Pos'].fillna(df['Pos'])
    return df

# q1=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8026',name_of_tournament='riviera',date=1)


# q1=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8026',name_of_tournament='riviera',date=1)
# q2=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8029',name_of_tournament='concession',date=2)
# q3=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8033',name_of_tournament='bay_hill',date=3)
# q4=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8038',name_of_tournament='sawgrass',date=4)
# q5=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8045',name_of_tournament='honda',date=5)
# q6=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8056',name_of_tournament='san_antonio',date=6)
# q7=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8060',name_of_tournament='masters',date=7)
# q8=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8064',name_of_tournament='harbour_town',date=8)
# q9=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8083',name_of_tournament='innisbrook',date=9)
# q10=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8091',name_of_tournament='quail_hollow',date=10)
# q11=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8098',name_of_tournament='craig_ranch',date=11)
# q12=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8102',name_of_tournament='kiawah_island',date=12)
# q13=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8108',name_of_tournament='colonial',date=13)
# q14=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8121',name_of_tournament='memorial',date=14)
# q15=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8134',name_of_tournament='congaree',date=15)
# q16=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8144',name_of_tournament='torrey_pines',date=16)
# q17=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8155',name_of_tournament='river_highlands',date=17)
# q18=clean_results(file_location='http://www.owgr.com/en/Events/EventResult.aspx?eventid=8170',name_of_tournament='detroit',date=18)
# all_results=pd.concat([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18])
# all_results.to_csv('C:/Users/Darragh/Documents/Python/Golf/results_csv.csv')
# st.write(all_results)

# df_test=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/results_csv.csv')
# df_test=df_test.rename(columns={'Name':'PLAYER NAME'})
# st.write(df_test)

# date_18 = pd.merge(combined_1, df_test,on=['PLAYER NAME','tournament','date'],how='outer')
# date_18.to_csv('C:/Users/Darragh/Documents/Python/Golf/date_18.csv')













# st.write('check combined', combined)

# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest",
# }
# # https://stackoverflow.com/questions/64501788/api-web-data-capture
# url = "https://www.pgatour.com/content/pgatour/stats/stat.02674.y2021.eon.t476.html"
# # url = "https://www.pgatour.com/content/pgatour/stats/stat.02564.y2021.eon.t476.html"

# df = pd.read_html(url, flavor="html5lib")
# df = pd.concat(df).drop([0, 1, 2], axis=1)
# st.write(df.head())


# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_476_southwind.pkl')
# df.to_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_476_southwind.pkl')

# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9204')
# table[0].to_pickle('C:/Users/Darragh/Documents/Python/Golf/results_southwind.pkl')
# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=179')
# table[0].to_pickle('C:/Users/Darragh/Documents/Python/Golf/results_scottish_open.pkl')




# RUN THIS FOR OGWR
# results_ogwr=clean_results('C:/Users/Darragh/Documents/Python/Golf/results_southwind.pkl','southwind',23)
# results_ogwr=results_ogwr.rename(columns={'Name':'PLAYER NAME'})
# st.write(results_ogwr)
# results_ogwr.to_pickle('C:/Users/Darragh/Documents/Python/Golf/results_southwind_ogwr.pkl')
# st.write('twin cities ogwr results', results_twin_cities)
# results_ogwr=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/results_southwind_ogwr.pkl')
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Cameron Davis'), 'PLAYER NAME' ] = 'Cam Davis'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Siwoo Kim'), 'PLAYER NAME' ] = 'Si Woo Kim'
# results_ogwr.loc [ (results_ogwr['PLAYER NAME']=='Kyoung-Hoon Lee'), 'PLAYER NAME' ] = 'K.H. Lee'


# st.write('change player names', results_ogwr[results_ogwr['PLAYER NAME'].str.contains('avis')])
# st.write('change player names', results_ogwr[results_ogwr['PLAYER NAME'].str.contains('Siwoo')])
# st.write('change player names', results_ogwr[results_ogwr['PLAYER NAME'].str.contains('Kyou')])

# x=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/twin_cities_stats.pkl')
# st.write(x)

# test=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/olympics_stats.pkl')
# st.write('stats??', test)


# def stats_results(event_ogwr=results_ogwr,stats_pickle='C:/Users/Darragh/Documents/Python/Golf/southwind_stats.pkl'):
#     # event_ogwr=pd.read_pickle(ogwr_pickle)
#     event_ogwr['Adj_Pos']=event_ogwr['Pos'].str.replace('WD','')
#     event_stats=pd.read_pickle(stats_pickle)
#     return pd.merge(event_stats, event_ogwr,on=['PLAYER NAME','tournament','date'],how='outer')

# result_stat_event=stats_results(event_ogwr=results_ogwr)
# result_stat_event.to_pickle('C:/Users/Darragh/Documents/Python/Golf/southwind_stats_results.pkl')
# result_stat_event=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/southwind_stats_results.pkl')
# st.write('check this stats/results of event', result_stat_event.head())
# st.write('check nan',result_stat_event[(result_stat_event['Pos'].isnull()) ])



# def combine_db(df, event_stats_results):
#     return pd.concat([df,event_stats_results],ignore_index=True)

# combine_db=combine_db(combined,result_stat_event)
# st.write('checking merge of event of stats and db', combine_db)

# combine_db.to_pickle('C:/Users/Darragh/Documents/Python/Golf/combined_1.pkl')

# results_deere_run=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/results_deere_run.pkl')

# results_deere_run=results_deere_run.rename(columns={'Name':'PLAYER NAME'})
# st.write('deere run', results_deere_run.head())
# my_updated_data = pd.merge(combined, results_deere_run,on=['PLAYER NAME','tournament','date'],how='outer')
# my_updated_data.to_pickle('C:/Users/Darragh/Documents/Python/Golf/data_stats_results_2.pkl')


# MIGHT NEED BELOW
# my_data=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/data_stats_results_1.pkl')
# st.write('my data', my_data.tail())
# combined_results=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/results_combined.pkl')
# combined_results=combined_results.rename(columns={'Name':'PLAYER NAME'})
# my_updated_data = pd.merge(my_data, results_deere_run,on=['PLAYER NAME','tournament','date','Pos','Ctry','R1','R2','R3','R4','Ranking Points','Adj_Pos','Agg'],how='outer')
# st.write('after merge', my_updated_data.tail())
# my_updated_data.to_pickle('C:/Users/Darragh/Documents/Python/Golf/merged_data.pkl')

# combined=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/data_stats_results.pkl')
# st.write('data stats results',combined.tail())
# test_1=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/data_stats_results_1.pkl')
# st.write('data stats results 1',test_1.tail())


# southwind=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02674_476_southwind.pkl')
# putt_southwind=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/_02564_476_southwind.pkl')






british_open=clean_results('C:/Users/Darragh/Documents/Python/Golf/results_british_open.pkl','british_open',20)
british_open=british_open.rename(columns={'Name':'PLAYER NAME'})
combined['Tee_App_Rank']=combined['Tee_App_Rank'].replace(np.NaN,75)
combined=combined.sort_values(by=['PLAYER NAME', 'date'])

# combined['Adj_Pos']=combined['Adj_Pos'].str.replace('T','')
# combined['Adj_Pos']=pd.to_numeric(combined['Adj_Pos'],errors='coerce')




def test_4(df):
    weights = np.array([0.125, 0.25,0.5,1])
    sum_weights = np.sum(weights)
    df['adj_tee_app_rank']=df['Tee_App_Rank'].rolling(window=4, center=False).apply(lambda x: np.sum(weights*x), raw=False)
    return df

grouped = combined.groupby('PLAYER NAME')
ranking_power=[]
for name, group in grouped:
    update=test_4(group)
    ranking_power.append(update)
df = pd.concat(ranking_power, ignore_index=True)
cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','adj_tee_app_rank','Pos']
cols = cols_to_move + [col for col in df if col not in cols_to_move]
combined=df[cols]
# st.write(df)

# st.write(combined.tail())
combined = pd.merge(combined, british_open,on=['PLAYER NAME','tournament','date','Pos','Ctry','R1','R2','R3','R4','Ranking Points','Adj_Pos','Agg'],how='outer')
# st.write('check to see if no.21 is in here keene trace', combined)

def merge_golf(tee_to_green_stats,putting_stats, name_of_tournament,date):
    tee_to_green_stats = tee_to_green_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','SG:APR','SG:ARG','SG:OTT']].copy()
    putting_stats = putting_stats.loc[:,['MEASURED ROUNDS','PLAYER NAME','ROUNDS','TOTAL SG:PUTTING']].copy()
    df = pd.merge(tee_to_green_stats, putting_stats, on=['PLAYER NAME', 'ROUNDS', 'MEASURED ROUNDS'])
    df['tournament']=name_of_tournament
    df['date']=date
    df=df.iloc[1:].copy()
    return df



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



format_dict = {'TOTAL SG:OTT':'{0:,.0f}','SG:OTT':'{0:,.0f}', 'SG:APR':'{0:,.0f}' ,'TOTAL SG:APR':'{0:,.0f}' ,'TOTAL SG:ARG':'{0:,.0f}', 'SG:ARG':'{0:,.0f}', 
'SG:PUTT':'{0:,.0f}' , 'SG: TOTAL':'{0:,.0f}' , 'SG: TOTAL_AVG':'{0:,.0f}', 'Rev_SG_Tot':'{0:,.1f}', 'TOTAL SG:PUTTING':'{0:,.0f}','sg_rank':'{0:,.0f}',
'app_sg_rank':'{0:,.0f}','ott_rank':'{0:,.0f}','arg_rank':'{0:,.0f}','normal_sg_no_putt':'{0:,.1f}','tee_green_normalised_sg':'{0:,.2f}',
'putt_rank':'{0:,.0f}','tee_to_green_rank':'{0:,.0f}','tee_green_rank':'{0:,.0f}','SG_Total':'{0:,.0f}','SG_Tee_Arg_Avg':'{0:,.1f}',
'SG_OTT':'{0:,.0f}','SG_APR':'{0:,.0f}','SG_ARG':'{0:,.0f}','SG_PUTT':'{0:,.0f}','SG_Total_Avg':'{0:,.1f}','Tee_Rank':'{0:,.0f}',
'adj_tee_app_rank':'{0:,.0f}',
'SG_Total_Avg_Rank':'{0:,.0f}','SG_Tee_Arg':'{0:,.0f}','SG_OTT_Avg':'{0:,.1f}','SG_APR_Avg':'{0:,.1f}','SG_ARG_Avg':'{0:,.1f}','SG_PUTT_Avg':'{0:,.1f}',
'PUTT_Rank':'{0:,.0f}','SG_OTT_Avg_Rank':'{0:,.0f}','Tee_App_Rank':'{0:,.0f}','ARG_Rank':'{0:,.0f}','TOTAL SG:TEE:ARG':'{0:,.0f}','SG_Rank':'{0:,.0f}',
'SG :Tee_Arg_AVG':'{0:,.1f}','Tee_Arg_Rank':'{0:,.0f}','SG_Rank_less_Rank':'{0:,.0f}','TOTAL SG:TEE_APR':'{0:,.0f}','TOTAL SG:TEE_ARG':'{0:,.0f}','Appr_Rank':'{0:,.0f}'  }

# event_stats=merge_golf(southwind, putt_southwind,'southwind',23)
# event_stats=clean_golf_tee(event_stats).reset_index()
# event_stats.to_pickle('C:/Users/Darragh/Documents/Python/Golf/southwind_stats.pkl')
# combined=pd.read_pickle('C:/Users/Darragh/Documents/Python/Golf/data_stats_results.pkl')
# combined = pd.concat([combined,deere_run_stats])


# combined = combined.reset_index()
# combined.to_pickle('C:/Users/Darragh/Documents/Python/Golf/combined_stats.pkl')


# st.write('this is combined database of the tournaments sorted by SG: TOTAL_AVG')
with st.beta_expander('Database sorted by Average Shots Gained from Tee to Putting for each Tournament'):
    st.write('This database gives an idea of who performed best across different tournaments')
    cols_to_move = ['PLAYER NAME','tournament','date','adj_tee_app_rank','Pos','Tee_App_Rank','Appr_Rank','Tee_Rank','ARG_Rank','PUTT_Rank','SG_Rank',
    'TOTAL SG:TEE_APR','TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING','SG: TOTAL',
    'SG: TOTAL_AVG','SG:OTT','SG:APR','SG:ARG','ROUNDS','MEASURED ROUNDS']
    cols = cols_to_move + [col for col in combined if col not in cols_to_move]
    combined=combined[cols]
    combined=combined.reset_index().drop('index',axis=1).sort_values(by='date',ascending=True)
    # st.write(combined.sort_values(by='adj_tee_app_rank',ascending=False).style.format(format_dict))
    
    st.write('Find a player')
    player_names=combined['PLAYER NAME'].unique()
    names_selected = st.multiselect('Select Player',player_names)
    st.write((combined.set_index('PLAYER NAME').loc[names_selected,:]).reset_index().sort_values(by='date',ascending=False).style.format(format_dict))

    st.write('Find a tournament')
    tournament_name=combined['tournament'].unique()
    tournament_names = st.multiselect('Select Tournament',tournament_name)
    st.write((combined.set_index('tournament').loc[tournament_names,:]).set_index('PLAYER NAME').style.format(format_dict))

with st.beta_expander('Last Tournament Played'):
    # last_date=st.number_input('what tournament number to include',value=22)
    # last_tournament_played=combined[combined['date']<(last_date+1)]
    last_tournament_played = combined.sort_values('date', ascending=False).drop_duplicates('PLAYER NAME').sort_values(by='SG: TOTAL_AVG',ascending=False)
    st.write('Last tournament played by Player')
    cols_to_move = ['PLAYER NAME','tournament','date','Tee_App_Rank','adj_tee_app_rank','Appr_Rank','Tee_Rank','PUTT_Rank','ARG_Rank','SG_Rank','Pos',
    'TOTAL SG:TEE_APR','TOTAL SG:OTT','TOTAL SG:APR','TOTAL SG:ARG','TOTAL SG:PUTTING','SG: TOTAL',
    'SG:OTT','SG:APR','SG:ARG','ROUNDS','MEASURED ROUNDS']
    cols = cols_to_move + [col for col in last_tournament_played if col not in cols_to_move]
    last_tournament_played=last_tournament_played[cols]
    last_tournament_played['adj_tee_app_rank']=last_tournament_played['adj_tee_app_rank'].fillna(1000)
    st.write(last_tournament_played.style.format(format_dict))
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
    # st.write(grouped_database_players[grouped_database_players['total_rounds']>min_rounds_played].sort_values(by='SG_Total_Avg',ascending=False).style.format(format_dict))
    # st.write(grouped_database_players.sort_values(by='SG_Total_Avg',ascending=False).style.format(format_dict))
    st.write('Find a player')
    grouped_database_players_index=grouped_database_players.reset_index()
    player_names_data=grouped_database_players_index['PLAYER NAME'].unique()
    names_selected_data = st.multiselect('Select Player',player_names_data)
    # st.write((grouped_database_players_index.set_index('PLAYER NAME').loc[names_selected_data,:]).style.format(format_dict))

st.write('check nan',combined[(combined['Pos'].isnull()) & (combined['MEASURED ROUNDS']>3) ])

with st.beta_expander('Notes'):
    st.write('when adding a major with no SG values, be careful, add this data in after the calculations are done')