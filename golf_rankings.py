from math import comb
from tkinter import CENTER
import streamlit as st
import pandas as pd
import numpy as np
import pathlib
import altair as alt
from st_aggrid import AgGrid, GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

st.set_page_config(layout="wide")

current_week=20
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

# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9514','uspga.csv')
# ogwr_file_csv_save('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9399','pebble_beach.csv')


# table=pd.read_html('http://www.owgr.com/en/Events/EventResult.aspx?eventid=9493')
# table[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/potomac.csv')
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

tournament_list=[masters,players, matchplay, riviera, bay_hill, scottsdale, kapalua, torrey_pines,innisbrook, jeddah, la_quinta,
dubai,hawaii,abu_dhabi,palm_beach,hilton_head, san_antonio, potomac,craig_ranch_texas,vidanta_mexico,pebble_beach, uspga]
combined=pd.concat(tournament_list,axis=0)

# events=pd.read_html('http://www.owgr.com/events')
# events[0].to_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events=pd.read_csv('C:/Users/Darragh/Documents/Python/Golf/rankings_data/ranking_events.csv')
ranking_events['World Rating']=pd.to_numeric(ranking_events['World Rating'],errors='coerce')
ranking_events['Event Name']=ranking_events['Event Name'].str.lower()
clean_ranking_event=ranking_events.loc[:,["Week","Year","Event Name","Winner's Points","World Rating","Home Rating","SoF"]]
with st.expander('Event'):
    st.write(clean_ranking_event.sort_values(by='World Rating', ascending=False))

    combined=pd.merge(combined,clean_ranking_event,on=["Event Name"],how='outer').reset_index().drop('index',axis=1)
    combined['Name']=combined['Name'].astype(str)

    # st.write('combined', combined.head())
    # st.write('combined', combined.shape)
    # st.write('combined shape', combined['Points Won'].dtype)
    combined=combined.sort_values(['Name','Week'],ascending=True)
    st.write(combined[combined['Event Name'].str.contains("u.s. pga championship")].sort_values(by=['Points Won'], ascending=False))

# combined['rolling_rank_pts']=combined.groupby(['Name'])['Points Won'].rolling(window=3,min_periods=1,center=False).mean().droplevel([0])
combined['rolling_rank_pts']=combined.groupby(['Name'])['Points Won'].expanding().mean().droplevel([0])
combined['rolling_rank_pts_sum']=combined.groupby(['Name'])['Points Won'].cumsum()
combined['rolling_rank_pts_count']=combined.groupby(['Name'])['Points Won'].cumcount()+1
combined['recalc_check']=(combined['rolling_rank_pts_sum']/combined['rolling_rank_pts_count'])-combined['rolling_rank_pts']
# st.write(combined.groupby(['Name'])['Points Won'].rolling(window=3,min_periods=1,center=False).mean().reset_index())
# combined['rolling_rank_pts']=combined.groupby(['Name'])['Points Won'].expanding(min_periods=1).sum()
cols_to_move = ['Name','Week','Event Name','Pos','Points Won','rolling_rank_pts','rolling_rank_pts_sum','rolling_rank_pts_count','recalc_check']
cols = cols_to_move + [col for col in combined if col not in cols_to_move]
combined=combined[cols]
# st.write('combined after name check Scheffler', combined[combined['Name'].str.contains('Nieman')])
st.write('Check on calc', combined[combined['recalc_check']>1])
st.write('Check on calc', combined[combined['recalc_check']<-1])
combined=combined.dropna(subset=['Points Won'])
combined=combined.sort_values(by=['Name','Week'],ascending=[True,True])
def test_4(df):
    weights = np.array([0.125, 0.25,0.5,1])
    # weights = np.array([1, 0.5,0.25,0.125])
    sum_weights = np.sum(weights)
    df['adj_exp_pts']=df['Points Won'].rolling(window=4, center=False).apply(lambda x: np.sum(weights*x), raw=False)
    return df

grouped = combined.groupby('Name')
ranking_power=[]
for name, group in grouped:
    update=test_4(group)
    ranking_power.append(update)
combined = pd.concat(ranking_power, ignore_index=True)

# st.write('combined', combined[combined['Name'].str.contains('nan')])
# format_dict = {'Points Won':'{0:,.0f}'}

with st.expander('Just graph min 3 events to see'):
    st.write('divide it up into deciles first')
    grouped_golfers=combined.groupby('Name').agg(number_events=('Week','count'),total_points=('Points Won','sum'),avg_points=('Points Won','mean')).reset_index()
    grouped_min_events=grouped_golfers[grouped_golfers['number_events']>4]
    grouped_min_events['avg_Rank']=(grouped_min_events['avg_points']).rank(method='dense', ascending=False).astype(int)
    grouped_min_events['Pts_Rank']=(grouped_min_events['total_points']).rank(method='dense', ascending=False).astype(int)
    grouped_min_events=grouped_min_events.sort_values(by='avg_Rank').reset_index().drop('index',axis=1)
    st.write(grouped_min_events)
    decile_df=grouped_golfers.groupby(pd.qcut(grouped_golfers['number_events'], q=8,duplicates='drop'))['Name'].count().reset_index()
    st.write(decile_df)
    decile_df_total_points=grouped_golfers.groupby(pd.qcut(grouped_golfers['total_points'], q=20,duplicates='drop'))['Name'].count().reset_index()
    st.write('Total Points decile',decile_df_total_points)
    decile_df_total_points=grouped_golfers.groupby(pd.qcut(grouped_golfers['avg_points'], q=24,duplicates='drop'))['Name'].count().reset_index()
    st.write('Total Points decile',decile_df_total_points)
    
    # st.write('combined', combined.head())
    combined_sort=combined.sort_values(by=['Name','Week'],ascending=[True,False]).loc[:,['Name','Week','Event Name','Points Won','Pos','adj_exp_pts','rolling_rank_pts',
    'rolling_rank_pts_count','rolling_rank_pts_sum']]
    top_20=combined_sort.copy()
    top_20['max_event']=top_20.groupby('Name')['rolling_rank_pts_count'].transform('max')
    top_20['latest_avg']=top_20.groupby('Name')['rolling_rank_pts'].transform('first')
    top_20=top_20[(top_20['max_event']>4) & (top_20['latest_avg']>8)]
    st.write('top 20', top_20)

    def graph_pl(decile_df_abs_home_1,column):
        line_cover= alt.Chart(decile_df_abs_home_1).mark_line().encode(alt.X('Week:O',axis=alt.Axis(title='Week',labelAngle=0)),
        alt.Y(column),color=alt.Color('Name'),tooltip=['Name'])
        # text_cover=line_cover.mark_text(baseline='middle',dx=0,dy=-15).encode(text=alt.Text(column),color=alt.value('black'))
        # overlay = pd.DataFrame({column: [0]})
        # vline = alt.Chart(overlay).mark_rule(color='black', strokeWidth=1).encode(y=column)
        # return st.altair_chart(line_cover + text_cover + vline,use_container_width=True)
        return st.altair_chart(line_cover,use_container_width=True)

    graph_pl(top_20,column='rolling_rank_pts')

with st.expander('Last 4 events'):
    st.write('Last say 4 events rolling avg for points')
    st.write('pick the week you want so lets say before week 15 which is masters')
    last_4=combined_sort[combined_sort['Week']<(current_week+1)].groupby('Name').head(4).reset_index()
    st.write('i want to get last 8 events in as well')
    # st.write('this is last 4', last_4)

    last_4['rolling_rank_pts_sum']=last_4.groupby(['Name'])['Points Won'].cumsum()
    last_4['rolling_rank_pts_count']=last_4.groupby(['Name'])['Points Won'].cumcount()+1
    last_4['rolling_rank_pts']=last_4.groupby(['Name'])['Points Won'].expanding().mean().droplevel([0])
    last_4['max_event']=last_4.groupby('Name')['rolling_rank_pts_count'].transform('max')
    
    last_4=last_4[(last_4['max_event']>3)]

    st.write(last_4[last_4['Name'].str.contains('Scheff')])
    grouped_golfers_last_4=last_4.groupby('Name').agg(number_events=('Week','count'),total_points=('Points Won','sum'),avg_points=('Points Won','mean'),
    exp_points=('adj_exp_pts','first')).reset_index()\
    .sort_values(by='avg_points',ascending=False)
    grouped_golfers_last_4['last_4_rank']=grouped_golfers_last_4['avg_points'].rank(method='dense', ascending=False).astype(int)
    grouped_golfers_last_4['exp_4_rank']=grouped_golfers_last_4['exp_points'].rank(method='dense', ascending=False).astype(int)
    grouped_golfers_last_4['total_rank']=(grouped_golfers_last_4['last_4_rank']+grouped_golfers_last_4['exp_4_rank']).rank(method='dense', ascending=True).astype(int)
    grouped_golfers_last_4=grouped_golfers_last_4.sort_values(by=['total_rank']).reset_index().drop('index',axis=1)
    st.write('Average Pts for last 4 events',grouped_golfers_last_4.sort_values(by=['total_rank']))

with st.expander('Last 8 events'):
    st.write('Last say 8 events rolling avg for points')
    st.write('pick the week you want so lets say before week 15 which is masters')
    number_of_events=8
    last_8=combined_sort[combined_sort['Week']<(current_week+1)].groupby('Name').head(number_of_events).reset_index()
    st.write('i want to get last 8 events in as well')
    # st.write('this is last 4', last_8)

    last_8['rolling_rank_pts_sum']=last_8.groupby(['Name'])['Points Won'].cumsum()
    last_8['rolling_rank_pts_count']=last_8.groupby(['Name'])['Points Won'].cumcount()+1
    last_8['rolling_rank_pts']=last_8.groupby(['Name'])['Points Won'].expanding().mean().droplevel([0])
    last_8['max_event']=last_8.groupby('Name')['rolling_rank_pts_count'].transform('max')
    
    last_8=last_8[(last_8['max_event']>(number_of_events-1))]

    st.write(last_8[last_8['Name'].str.contains('Zala')])
    grouped_golfers_last_8=last_8.groupby('Name').agg(number_events=('Week','count'),total_points=('Points Won','sum'),avg_points=('Points Won','mean'),
    exp_points=('adj_exp_pts','first'),median_points=('Points Won','median'),Week=('Week','first')).reset_index()\
    .sort_values(by='avg_points',ascending=False)
    grouped_golfers_last_8['last_8_rank']=grouped_golfers_last_8['avg_points'].rank(method='dense', ascending=False).astype(int)
    grouped_golfers_last_8['exp_4_rank']=grouped_golfers_last_8['exp_points'].rank(method='dense', ascending=False).astype(int)
    grouped_golfers_last_8['median_rank']=grouped_golfers_last_8['median_points'].rank(method='dense', ascending=False).astype(int)
    grouped_golfers_last_8['total_med_rank']=(grouped_golfers_last_8['last_8_rank']+grouped_golfers_last_8['median_rank']).rank(method='dense', ascending=True).astype(int)
    grouped_golfers_last_8['total_rank']=(grouped_golfers_last_8['last_8_rank']+grouped_golfers_last_8['exp_4_rank']).rank(method='dense', ascending=True).astype(int)
    grouped_golfers_last_8=grouped_golfers_last_8.sort_values(by=['total_rank']).reset_index().drop('index',axis=1)

    # st.write('number',max(grouped_golfers_last_8['Week']))
    week_after_event=combined_sort[combined_sort['Week']>(max(grouped_golfers_last_8['Week']))].rename(columns={'Pos':'pos_next_event','Points Won':'points_next_event'})\
    .loc[:,['Name','pos_next_event','points_next_event']]
    # week_after_event=week_after_event.loc[:,['Name','pos_next_event']]
    # st.write('this is week after event of combined',week_after_event)
    grouped_golfers_last_8=pd.merge(grouped_golfers_last_8,week_after_event,on='Name',how='left')
    grouped_golfers_last_8['points_next_event']=grouped_golfers_last_8['points_next_event'].fillna(0)
    grouped_golfers_last_8['cum_median_rank']=grouped_golfers_last_8['median_rank'].cumsum()
    grouped_golfers_last_8['test']=grouped_golfers_last_8['number_events'].cumsum()
    grouped_golfers_last_8=grouped_golfers_last_8.sort_values(by=['points_next_event'],ascending=False)
    grouped_golfers_last_8=grouped_golfers_last_8.reset_index().drop('index',axis=1)
    cols_to_move = ['Name','number_events','Week','last_8_rank','median_rank','total_med_rank','pos_next_event','total_rank','points_next_event','cum_median_rank','test']
    cols = cols_to_move + [col for col in grouped_golfers_last_8 if col not in cols_to_move]
    grouped_golfers_last_8=grouped_golfers_last_8[cols].sort_values(by=['points_next_event'],ascending=False)
    st.write('Average Pts for last 8 events',grouped_golfers_last_8)

    gb = GridOptionsBuilder.from_dataframe(grouped_golfers_last_8)
    gb.configure_column("total_points", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("avg_points", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("exp_points", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("median_points", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    gb.configure_column("points_next_event", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0, aggFunc='sum')
    # gb.configure_column("Date", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='dd-MM-yyyy', pivot=True)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()
    grid_response = AgGrid(
        grouped_golfers_last_8, 
        gridOptions=gridOptions,
        # height=grid_height, 
        width='100%',
        # data_return_mode=return_mode_value, 
        # update_mode=update_mode_value,
        # fit_columns_on_grid_load=fit_columns_on_grid_load,
        allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
        enable_enterprise_modules=True,
    )
    # AgGrid(grouped_golfers_last_8)

with st.expander("Player Detail"):
    st.write('combined', combined.head())
    st.write('Find a player')
    player_names=combined['Name'].unique()
    names_selected = st.multiselect('Select Player',player_names)
    st.write((combined.set_index('Name').loc[names_selected,:]).reset_index().sort_values(by='Week',ascending=False))

with st.expander('Filter Combined Analysis by week'):

    # week_pick=18
    week_pick=st.number_input("Select the week",value=15, step=1)
    # week_selection=((combined.set_index('Week').loc[week_pick,:]).reset_index())
    week_selection=combined[combined['Week']<week_pick].copy()

    def analysis_golf(combined):
        filtered = combined.groupby('Name').agg(ranking_points_total=('Points Won','sum'),tournaments_played=('Points Won','count'),
        avg_ranking_points=('Points Won','mean'))
        filtered['avg_ranking_points_Rank']=(filtered['avg_ranking_points']).rank(method='dense', ascending=False)
        filtered['avg_ranking_points_Rank']=filtered['avg_ranking_points_Rank']
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

