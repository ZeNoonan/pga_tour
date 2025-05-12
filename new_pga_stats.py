import streamlit as st
import pandas as pd
import numpy as np
import pathlib
import altair as alt
from itertools import product, combinations
st.set_page_config(layout="wide")

# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/tournaments/2024/the-players-championship/R2024011.html')))
# st.write(a)

# st.write('')

# st.write('look at will zalatoris to see why not picking up in handicap graph????')

with st.expander('World Rankings'):
    def ogwr_file_csv_save(url_comp,filename_ext):
        table=pd.read_html(url_comp)
        p=pathlib.Path.cwd().joinpath('golf','rankings_data')
        return table[0].to_csv(p.joinpath(filename_ext))

    

    def clean_results(file_location,name_of_tournament,year,date):
        df=pd.read_csv(file_location)
        df['Event Name']=name_of_tournament
        df['year']=int(year)
        df['position']=df['Finish Pos.'].str.extract('(\d+)')
        df['position']=df['position'].fillna(999)
        df['position']=pd.to_numeric(df['position'])
        df['date']=pd.to_datetime(date, dayfirst=True) # KEEP AN EYE ON THIS, DATES WERE NOT BEING READ IN CORRECTLY DUE TO EURO/US Format date        
        df=df.dropna(subset=['Finish Pos.'])
        df['NAME']=df['NAME'].str.title()
        df['MC']=np.where(df['Finish Pos.'].isin(['MC', 'WD']),np.NaN,1)

        df['miss_cut']=np.where(df['Finish Pos.'].isin(['MC', 'WD']),1,np.NaN)
        df=df.loc[:,~df.columns.str.contains("Unnamed: 0|POINTS WON|RANK FROM|RANK TO|CTRY", case=False)]
        # df=df.loc[:,~(df['Finish Pos.'].str.contains("WD", case=False))]
        # df=df[~df['Finish Pos.'].str.contains("WD")].copy()    
        # df=df.drop(df.columns.str.contains("Unnamed: 0|R1|R2|R3|R4|CTRY",axis=1, na=False))
        # df=df.drop(['Unnamed: 0',"R1","R2","R3","R4",'CTRY'],axis=1)
        df['AGG']=pd.to_numeric(df['AGG'],errors='ignore')

        return df
    
    # using this for Barracuda as its stableford competition
    def clean_results_stableford(file_location,name_of_tournament,year,date):
        df=pd.read_csv(file_location)
        df['Event Name']=name_of_tournament
        df['year']=int(year)
        df['position']=df['Finish Pos.'].str.extract('(\d+)')
        df['position']=df['position'].fillna(999)
        df['position']=pd.to_numeric(df['position'])
        df['date']=pd.to_datetime(date)        
        df=df.dropna(subset=['Finish Pos.'])
        df['NAME']=df['NAME'].str.title()
        df['MC']=np.where(df['Finish Pos.'].isin(['MC', 'WD']),np.NaN,1)

        df['miss_cut']=np.where(df['Finish Pos.'].isin(['MC', 'WD']),1,np.NaN)
        df=df.loc[:,~df.columns.str.contains("Unnamed: 0|POINTS WON|RANK FROM|RANK TO|CTRY", case=False)]
        # df=df.loc[:,~(df['Finish Pos.'].str.contains("WD", case=False))]
        # df=df[~df['Finish Pos.'].str.contains("WD")].copy()    
        # df=df.drop(df.columns.str.contains("Unnamed: 0|R1|R2|R3|R4|CTRY",axis=1, na=False))
        # df=df.drop(['Unnamed: 0',"R1","R2","R3","R4",'CTRY'],axis=1)
        # df['AGG']=pd.to_numeric(df['AGG'],errors='ignore')

        return df

    # ogwr_file_csv_save("https://www.owgr.com/events/the-sentry-10690",'kapalua_2025.csv')
    # ogwr_file_csv_save("https://www.owgr.com/events/sony-open-in-hawaii-10691",'hawaii_2025.csv')
    # ogwr_file_csv_save("https://www.owgr.com/events/valero-texas-open-10777",'san_antonio_2025.csv')    
    # ogwr_file_csv_save("https://www.owgr.com/events/rbc-heritage-10793",'harbour_town_2025.csv')    
    ogwr_file_csv_save("https://www.owgr.com/events/truist-championship-10825",'philadelphia_2025.csv')    
    memphis_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/memphis_2024.csv','memphis',2024,pd.to_datetime('18-08-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    wyndham_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/wyndham_2024.csv','wyndham',2024,pd.to_datetime('11-08-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    olympics_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/olympics_2024.csv','olympics',2024,pd.to_datetime('04-08-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    minnesota_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/minnesota_2024.csv','minnesota',2024,pd.to_datetime('28-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    troon_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/troon_2024.csv','troon',2024,pd.to_datetime('21-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    barracuda_2024=clean_results_stableford('C:/Users/Darragh/Documents/Python/Golf/rankings_data/barracuda_2024.csv','barracuda',2024,pd.to_datetime('21-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    kentucky_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/kentucky_2024.csv','kentucky',2024,pd.to_datetime('14-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    scottish_open_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/scottish_open_2024.csv','scottish_open',2024,pd.to_datetime('14-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    chicago_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/chicago_2024.csv','chicago',2024,pd.to_datetime('07-07-2024',dayfirst=True)).rename(columns={'NAME':'Name'})     
    detroit_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/detroit_2024.csv','detroit',2024,pd.to_datetime('30-06-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    tpc_river_highlands_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/tpc_river_highlands_2024.csv','tpc_river_highlands',2024,pd.to_datetime('23-06-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    pinehurst_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/pinehurst_2024.csv','pinehurst',2024,pd.to_datetime('16-06-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    memorial_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/memorial_2024.csv','memorial',2024,pd.to_datetime('06-06-2024',dayfirst=True)).rename(columns={'NAME':'Name'})     
    canada_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/canada_2024.csv','canada',2024,pd.to_datetime('30-05-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    colonial_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/colonial_2024.csv','colonial',2024,pd.to_datetime('26-05-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    valhalla_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/valhalla_2024.csv','Valhalla',2024,pd.to_datetime('19-05-2024',dayfirst=True)).rename(columns={'NAME':'Name'})    
    quail_hollow_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/quail_hollow_2024.csv','Quail_Hollow',2024,pd.to_datetime('12-05-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    dallas_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/dallas_2024.csv','Dallas',2024,pd.to_datetime('05-05-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    Hilton_Head_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/Hilton_Head_2024.csv','Hilton_Head',2024,'21-04-2024').rename(columns={'NAME':'Name'})
    masters_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2024.csv','Masters',2024,'14-04-2024').rename(columns={'NAME':'Name'})
    san_antonio_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/San_Antonio_2024.csv','San_Antonio',2024,pd.to_datetime('07-04-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    houston_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/Houston_2024.csv','Houston',2024,'31-03-2024').rename(columns={'NAME':'Name'})
    tampa_bay_2024=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/tampa_bay_2024.csv','tampa_bay',2024,'24-03-2024').rename(columns={'NAME':'Name'})
    sawgrass=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/sawgrass_2024.csv','sawgrass',2024,'24-03-2024').rename(columns={'NAME':'Name'})
    api=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/api_2024.csv','api',2024,pd.to_datetime('10-03-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    west_palm_beach=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/west_palm_beach_2024.csv','west_palm_beach',2024,pd.to_datetime('03-03-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    west_palm_beach_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/west_palm_beach_2025.csv','west_palm_beach_2025',2024,pd.to_datetime('02-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})    
    mexico=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/mexico_2024.csv','mexico',2024,pd.to_datetime('25-02-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    mexico_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/mexico_2025.csv','mexico_2025',2025,pd.to_datetime('23-02-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    riviera=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/riviera_2024.csv','riviera',2024,'18-02-2024').rename(columns={'NAME':'Name'})
    torrey_riviera_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/torrey_riviera_2025.csv','torrey_riviera_2025',2025,'16-02-2025').rename(columns={'NAME':'Name'})
    phoenix=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/phoenix_2024.csv','phoenix',2024,pd.to_datetime('11-02-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    phoenix_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/phoenix_2025.csv','phoenix_2025',2025,pd.to_datetime('09-02-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    pebble_beach=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/pebble_beach_2024.csv','pebble_beach',2024,pd.to_datetime('04-02-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    pebble_beach_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/pebble_beach_2025.csv','pebble_beach',2025,pd.to_datetime('02-02-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    torrey_pines=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/torrey_pines_2024.csv','torrey_pines',2024,'27-01-2024').rename(columns={'NAME':'Name'})
    torrey_pines_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/torrey_pines_farmers_2025.csv','torrey_pines_farmers',2025,'26-01-2025').rename(columns={'NAME':'Name'})
    palm_springs_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/palm_springs_2025.csv','palm_springs',2025,'19-01-2025').rename(columns={'NAME':'Name'})
    hawaii=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/hawaii_2024.csv','hawaii',2024,'14-01-2024').rename(columns={'NAME':'Name'})
    hawaii_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/hawaii_2025.csv','hawaii',2025,'12-01-2025').rename(columns={'NAME':'Name'})
    kapalua=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/kapalua_2024.csv','kapalua',2024,pd.to_datetime('07-01-2024',dayfirst=True)).rename(columns={'NAME':'Name'})
    kapalua_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/kapalua_2025.csv','kapalua',2025,pd.to_datetime('05-01-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    dubai_desert_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/dubai_desert_2025.csv','dubai_desert',2025,pd.to_datetime('19-01-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    bay_hill_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/bay_hill_2025.csv','bay_hill_2025',2025,pd.to_datetime('09-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    puerto_rico_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/puerto_rico_2025.csv','puerto_rico_2025',2025,pd.to_datetime('10-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    players_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/players_2025.csv','players_2025',2025,pd.to_datetime('16-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})    
    innisbrook_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/innisbrook_2025.csv','innisbrook_2025',2025,pd.to_datetime('23-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    houston_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/houston_2025.csv','houston_2025',2025,pd.to_datetime('30-03-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    san_antonio_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/san_antonio_2025.csv','san_antonio_2025',2025,pd.to_datetime('06-04-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    masters_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/masters_2025.csv','masters_2025',2025,pd.to_datetime('13-04-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    harbour_town_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/harbour_town_2025.csv','harbour_town_2025',2025,pd.to_datetime('20-04-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    craig_ranch_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/craig_ranch_2025.csv','craig_ranch_2025',2025,pd.to_datetime('04-05-2025',dayfirst=True)).rename(columns={'NAME':'Name'})    
    philadelphia_2025=clean_results('C:/Users/Darragh/Documents/Python/Golf/rankings_data/philadelphia_2025.csv','philadelphia_2025',2025,pd.to_datetime('11-05-2025',dayfirst=True)).rename(columns={'NAME':'Name'})
    combined_data=pd.concat([memphis_2024,wyndham_2024,olympics_2024,minnesota_2024,troon_2024,barracuda_2024,kentucky_2024,scottish_open_2024,chicago_2024,detroit_2024,tpc_river_highlands_2024,pinehurst_2024,memorial_2024,canada_2024,colonial_2024,valhalla_2024,quail_hollow_2024,dallas_2024,Hilton_Head_2024,masters_2024,san_antonio_2024,houston_2024,tampa_bay_2024,sawgrass,api,west_palm_beach,mexico,riviera,phoenix,
                             pebble_beach,torrey_pines,hawaii,kapalua,kapalua_2025,hawaii_2025,palm_springs_2025,pebble_beach_2025,
                             phoenix_2025,torrey_pines_2025,dubai_desert_2025,torrey_riviera_2025,mexico_2025,west_palm_beach_2025, puerto_rico_2025,
                               bay_hill_2025,players_2025,masters_2025,harbour_town_2025,san_antonio_2025,
                               innisbrook_2025,houston_2025,craig_ranch_2025,philadelphia_2025,
                               ])
    # combined_data_2025=pd.concat([kapalua_2025,hawaii_2025,palm_springs_2025])
    def round(combined_data):
        combined_data["R1"]=pd.to_numeric(combined_data["R1"],errors='coerce')
        combined_data["R2"]=pd.to_numeric(combined_data["R2"],errors='coerce')
        combined_data["R3"]=pd.to_numeric(combined_data["R3"],errors='coerce')
        combined_data["R4"]=pd.to_numeric(combined_data["R4"],errors='coerce')
        combined_data["AGG"]=pd.to_numeric(combined_data["AGG"],errors='coerce')
        return combined_data
    
    combined_data=round(combined_data)
    # combined_data_2025=round(combined_data_2025)
    # st.write('zala detroit', detroit_2024)
    # st.write(combined_data.dtypes)
    # st.write(combined_data)
    # st.write(pinehurst_2024)
    # combined_data.to_parquet('C:/Users/Darragh/Documents/Python/Golf/golf_results_from_ogwr.parq')

    # st.write('comb', combined_data)
    # st.write('hil', masters_2024)
    # df['var']=df[]

# with st.expander('sawgrass detail perf'):
#     sawgrass_par_3_performance=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_par_3_performance.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_par_3'}).set_index('PLAYER')

#     sawgrass_bogey_avoidance=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_bogey_avoidance.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_bogey_avoid'}).set_index('PLAYER')
#     sawgrass_gir_fringe=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_gir_fringe.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_gir'}).set_index('PLAYER')
#     # st.write('sawgrass_gir_fringe',sawgrass_gir_fringe)
#     # sawgrass_gir=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_gir.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_gir'}).set_index('PLAYER')
#     # st.write('sawgrass_gir',sawgrass_gir)
#     sawgrass_sg_approach=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_sg_approach.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_sg_app'}).set_index('PLAYER')
#     st.write('sawgrass_sg_approach',sawgrass_sg_approach)
#     sawgrass_distance_edge_fairway=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_distance_edge_fairway.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_dist_edge_fwy'}).set_index('PLAYER')

#     sawgrass_driving_distance=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_driving_distance.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_driv_dist'}).set_index('PLAYER')
#     sawgrass_ball_striking=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_ball_striking.csv')
#     sawgrasss_total_driving=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrasss_total_driving.csv')
#     # sawgrass_dist_fairway_centre=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_dist_fairway_centre.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_dist_centre_fwy'}).set_index('PLAYER')
#     sawgrass_fairway_percent = pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_fairway_%.csv').loc[:,['PLAYER','RANK','FAIRWAYS HIT','POSSIBLE FAIRWAYS','%']]\
#         .rename(columns={'RANK':'rank_fwy_percent','%':'fwy_%'}).set_index('PLAYER')
#     sawgrass_fairway_percent['fwy_%'] = sawgrass_fairway_percent['FAIRWAYS HIT'] / sawgrass_fairway_percent['POSSIBLE FAIRWAYS']
#     sawgrass_sg_tee=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/sawgrass_sg_tee.csv').loc[:,['PLAYER','RANK']].rename(columns={'RANK':'rank_sg_tee'}).set_index('PLAYER')

#     # st.write('sawgrass fairway',sawgrass_fairway_percent)
#     # st.write('sawgrass fairway',sawgrass_fairway_percent['fwy_%'].max())
#     sawgrass_ranks=pd.concat([sawgrass_par_3_performance,sawgrass_bogey_avoidance,sawgrass_gir_fringe,sawgrass_sg_approach,
#                             sawgrass_distance_edge_fairway,sawgrass_driving_distance,sawgrass_fairway_percent,
#                             sawgrass_sg_tee],axis=1)

#     # idea behind this is to reward fairways hit proportionaly with left over being the missed fairway and how much it was missed by
#     sawgrass_ranks['fwy_plus_missed'] = ( ((sawgrass_ranks['rank_fwy_percent']* ( sawgrass_ranks['fwy_%'].max() )) + (sawgrass_ranks['rank_dist_edge_fwy']* ( 1-(sawgrass_ranks['fwy_%'].max()) ))).\
#                                         rank(method='dense', ascending=True) )
#     off_tee_perf = sawgrass_ranks.loc[:,['rank_sg_tee','fwy_plus_missed','rank_driv_dist','rank_fwy_percent','rank_dist_edge_fwy','FAIRWAYS HIT','POSSIBLE FAIRWAYS']]
#     st.write('off tee perf',off_tee_perf)

#     appr_perf = sawgrass_ranks.loc[:,['rank_par_3','rank_sg_app']]

#     st.write("sawgrass_approach_performance",appr_perf)

#     st.write('general',sawgrass_ranks)
with st.expander('Masters Analysis Historical'):

    def highlight_max(cell): 
        if type(cell) != str and cell < 0 : 
            return 'background: blue; color:black'
        else: 
            return 'background: black; color: white'
        
    def highlight_max(cell):   # sourcery skip: assign-if-exp
        if type(cell) != str and cell < 0 : 
            return 'color: red'
        else: 
            return 'color: green'

    golf_historical = pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx')
    golf_historical['Amount']=golf_historical['Amount'].replace({'np.NaN':np.NaN})
    golf_historical['Amount']=golf_historical['Amount'].replace({'np.nan':np.NaN})
    golf_historical['Amount']=golf_historical['Amount'].replace({'np.NAN':np.NaN})
    golf_historical['Amount']=pd.to_numeric(golf_historical['Amount'])


    # lsat_3_tourn = golf_historical['Tournament']<3
    not_equal_zero_approx = golf_historical['Amount']>0.05
    not_equal_zero_approx_1 = golf_historical['Amount']<-0.05
    # golf_historical['new_amount'] = golf_historical['Amount'].where(lsat_3_tourn)
    golf_historical['amount_last_3'] = golf_historical['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(golf_historical['Tournament']<3)
    golf_historical['amount_last_4'] = golf_historical['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(golf_historical['Tournament']<4)
    # st.write('FIX THIS HERE')
    # st.write(golf_historical)
    # st.write(golf_historical.dtypes)

    # golf_historical['sum_factors']=np.where( ((golf_historical['Amount']>=-0.05) & (golf_historical['Amount'] <= 0.05)),0
    #                                         ,np.where(golf_historical['Amount']>0.05,1,np.where(golf_historical['Amount']<0.05,-1,np.NaN)))
    golf_historical['positive_factors_last_4']=np.where(golf_historical['amount_last_4']>0.05,1,np.NaN)
    golf_historical['positive_factors_last_3']=np.where(golf_historical['amount_last_3']>0.05,1,np.NaN)
    # st.write(golf_historical)
    groupby_factors=golf_historical.groupby('Year').agg(positive_factors_last_3=('positive_factors_last_3','sum'),count_factors_last_3=('amount_last_3','count'),
                    positive_factors_last_4=('positive_factors_last_4','sum'),count_factors_last_4=('amount_last_4','count'),
                    )

    # groupby_factors['%_coverage']=groupby_factors['sum_factors'] / groupby_factors['count_factors']
    groupby_factors['diff_last_3']=groupby_factors['positive_factors_last_3'] - groupby_factors['count_factors_last_3']
    groupby_factors['diff_last_4']=groupby_factors['positive_factors_last_4'] - groupby_factors['count_factors_last_4']
    groupby_factors['%_positive_last_3']=groupby_factors['positive_factors_last_3'] / groupby_factors['count_factors_last_3']
    groupby_factors['%_positive_last_4']=groupby_factors['positive_factors_last_4'] / groupby_factors['count_factors_last_4']
    st.write(groupby_factors.sort_values(by=['Year'],ascending=False))
    data={'Rahm_2023_app':[-1.18,2.19,.59,3.15],'Rahm_2023_arg':[0.36,1.34,.67,-.05],
        'Scheffler_2022_app':[-.72,2.18,1.66,-.26],'Scheffler_2022_arg':[.19,.36,.61,.75],
        'Hideki_2021_app':[.82,1.33,1.14,.74],'Hideki_2021_arg':[1.09,.28,-.14,1.69],
        'Dustin_2020_app':[.83,1.99,np.NaN,np.NaN],'Dustin_2020_arg':[.47,.52,np.NaN,np.NaN],
        'Tiger_2019_app':[-.82,2.35,.52,1.43],'Tiger_2019_arg':[.66,1.06,.34,.35],
        'Reed_2018_app':[-.01,2.15,.29,-1.85],'Reed_2018_arg':[.96,.61,.75,.72],
        'Sergio_2017_app':[.46,.47,.24,np.NAN],'Sergio_2017_arg':[.18,.48,.73,np.NAN],
        'Willett_2016_app':[.74,.77,np.nan,np.nan],'Willett_2016_arg':[.77,1.02,np.nan,np.nan],
        'Spieth_2015_app':[1.21,.74,1.14,-1.15],'Spieth_2015_arg':[.48,.25,1.19,.64],
        'Bubba_2014_app':[.28,-.03,1.11,.08],'Bubba_2014_arg':[-.86,.4,.19,.37],
        'Scott_2013_app':[.12,1.13,.89,np.nan],'Scott_2013_arg':[.03,.8,1.03,np.nan],
        'Bubba_2012_app':[.83,1.41,.7,1.31],'Bubba_2012_arg':[.5,-.21,-.01,.17],
        'Schwartzel_2011_app':[.23,-.96,.59,.63],'Schwartzel_2011_arg':[-.33,.27,.23,.01],
        'Phil_2010_app':[.85,1.1,1.33,1.04],'Phil_2010_arg':[.86,-.2,1.12,-.17]}

    ott_data={'Rahm_ott':[.31,.61,-1.46,.26],'Scheffler_ott':[.41,.07,-.03,1.4],'Hideki_ott':[-.82,.07,.45,-.16],'Dustin_ott':[1.35,.73,np.nan,np.nan],
        'Tiger_ott':[1.28,-1,.65,.25],'Reed_ott':[.29,.53,.35,-.14],'Sergio_ott':[1.63,1.23,1.06,np.nan],'Willett_ott':[.37,.76,np.nan,np.nan],
        'Spieth_ott':[1.17,.59,.22,.94],'Bubba_2014_ott':[-7.65,1.78,1.84,1.95],'Scott_ott':[.88,1.59,.48,np.nan],'Bubba_2012_ott':[1.62,1.58,1.59,1.87],
        'Schwartzel_ott':[.99,.75,.28,.12],'Phil_ott':[-.27,-.76,.47,.45]}

    return_data=pd.DataFrame(data)
    st.write(return_data.style.applymap(highlight_max))
    st.write(pd.DataFrame(ott_data).style.applymap(highlight_max))

# with st.expander('current'):
#     current_data=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Current')
#     tournie_id=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Tournament_Listing_Chrono')
#     current_data=pd.merge(current_data,tournie_id,how='left',on='Tour_Name').sort_values(by=['Name','Tournament'],ascending=[True,True]).reset_index()
#     current_data['Name']=current_data['Name'].str.title()
#     current_data['Tournament']=pd.to_numeric(current_data['Tournament'])
#     current_data_before_rank=current_data.copy()
#     current_data['event_tracker']=current_data.groupby('Name')['Tournament'].rank(method='first', ascending=True)
#     # st.write('after concat', current_data)
#     # st.write(current_data)
#     def analysis_data(current_data):
#         not_equal_zero_approx = current_data['Amount']>0.05
#         not_equal_zero_approx_1 = current_data['Amount']<-0.05
#         current_data['amount_last_3'] = current_data['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(current_data['event_tracker']<10)
#         current_data['amount_last_4'] = current_data['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(current_data['event_tracker']<13)
#         current_data['amount_last_1'] = current_data['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(current_data['event_tracker']<4)
#         # current_data['amount_last_3_test'] = current_data['Amount'].where(not_equal_zero_approx | not_equal_zero_approx_1).where(current_data['Tournament']<4)
#         # st.write('FIX THIS HERE')
#         # st.write(current_data)
#         # st.write(golf_historical.dtypes)

#         # golf_historical['sum_factors']=np.where( ((golf_historical['Amount']>=-0.05) & (golf_historical['Amount'] <= 0.05)),0
#         #                                         ,np.where(golf_historical['Amount']>0.05,1,np.where(golf_historical['Amount']<0.05,-1,np.NaN)))
#         current_data['positive_factors_last_4']=np.where(current_data['amount_last_4']>0.05,1,np.NaN)
#         current_data['positive_factors_last_3']=np.where(current_data['amount_last_3']>0.05,1,np.NaN)
#         current_data['positive_factors_last_1']=np.where(current_data['amount_last_1']>0.05,1,np.NaN)
#         # st.write(golf_historical)
#         groupby_factors=current_data.groupby('Name').agg(positive_factors_last_3=('positive_factors_last_3','sum'),count_factors_last_3=('amount_last_3','count'),
#                         positive_factors_last_4=('positive_factors_last_4','sum'),count_factors_last_4=('amount_last_4','count'),
#                         positive_factors_last_1=('positive_factors_last_1','sum'),count_factors_last_1=('amount_last_1','count'),
#                         )

#         # groupby_factors['%_coverage']=groupby_factors['sum_factors'] / groupby_factors['count_factors']
#         groupby_factors['diff_last_3']=groupby_factors['positive_factors_last_3'] - groupby_factors['count_factors_last_3']
#         groupby_factors['diff_last_4']=groupby_factors['positive_factors_last_4'] - groupby_factors['count_factors_last_4']
#         groupby_factors['diff_last_1']=groupby_factors['positive_factors_last_1'] - groupby_factors['count_factors_last_1']
#         groupby_factors['%_positive_last_3']=groupby_factors['positive_factors_last_3'] / groupby_factors['count_factors_last_3']
#         groupby_factors['%_positive_last_4']=groupby_factors['positive_factors_last_4'] / groupby_factors['count_factors_last_4']
#         return groupby_factors


#     groupby_factors=analysis_data(current_data)
#     st.write('Last 3',groupby_factors.sort_values(by='diff_last_3',ascending=False).reset_index())
#     st.write('Last 1',groupby_factors.sort_values(by=['diff_last_1','diff_last_3'],ascending=[False,False]).reset_index())
#     st.write('Bottom of the Pack',groupby_factors.sort_values(by='diff_last_3',ascending=True))

# with st.expander('Houston'):
#     updated_groupby_factors=groupby_factors.reset_index()
#     # houston_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Houston',header=None).values.tolist()
#     houston_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Houston')
#     # st.write('houst',houston_players)
#     houston_merge=pd.merge(updated_groupby_factors,houston_players,on='Name',how='right')
#     # houston_merge.index=houston_players.index
#     # houston_merge['No.']=range(len(houston_merge))
#     # houston_merge=houston_merge.reset_index()
#     st.write('houston', houston_merge.sort_values(by='diff_last_3',ascending=False).reset_index(drop=True))
#     # houston_players_dict=houston_players.to_dict()
#     # st.write('dict', houston_players_dict)
#     # st.write(updated_groupby_factors[updated_groupby_factors['Name'].isin(houston_players_dict)])
#     # st.write(updated_groupby_factors[updated_groupby_factors['Name'].isin(houston_players)])
#     # st.write(updated_groupby_factors)
#     # updated_groupby_factors['Houston_Players'] = updated_groupby_factors[]

# with st.expander('San Antonio'):
#     pre_masters_data=current_data_before_rank[(current_data_before_rank['Tournament']>1)]
#     st.write('Tournies played before San Antonio',pre_masters_data.groupby(['Name']).agg(number=('Tournament','nunique')))
#     pre_masters_data=pre_masters_data.drop('index',axis=1).sort_values(by=['Name','Tournament'],ascending=[True,True]).reset_index(drop=True)
#     pre_masters_data['event_tracker']=pre_masters_data.groupby('Name')['Tournament'].rank(method='first', ascending=True)

#     updated_groupby_factors=analysis_data(pre_masters_data).reset_index()
#     master_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='San Antonio')
#     master_players['Name']=master_players['Name'].str.title()
#     # st.write('San Antonio', master_players)
#     houston_merge=pd.merge(updated_groupby_factors,master_players,on='Name',how='right')
#     final_masters_results=pd.merge(houston_merge,san_antonio_2024.loc[:,['Name','position']],on='Name',how='left').sort_values(by='position')
#     st.write('Final Result',final_masters_results.loc[:,['Name','diff_last_3','diff_last_1','position']])

# with st.expander('Masters'):
#     st.write('My takeaway here is that betting on Top 40 for every player who has 0 negatives in the week prior in the SG categories ott app arg')
#     st.write('looks profitable')
#     # current_data_before_rank=current_data.copy()
#     pre_masters_data=current_data_before_rank[current_data_before_rank['Tour_Name']!='Masters']
#     pre_masters_data=pre_masters_data.drop('index',axis=1).sort_values(by=['Name','Tournament'],ascending=[True,True]).reset_index(drop=True)
#     # st.write('pre ranking sort', pre_masters_data[pre_masters_data['Name'].str.contains('Fleetwood')])
#     pre_masters_data['event_tracker']=pre_masters_data.groupby('Name')['Tournament'].rank(method='first', ascending=True)
#     # st.write('after ranking', pre_masters_data[pre_masters_data['Name'].str.contains('Fleetwood')])

#     updated_groupby_factors=analysis_data(pre_masters_data).reset_index()
#     # st.write('after function', updated_groupby_factors[updated_groupby_factors['Name'].str.contains('Fleetwood')])
#     # houston_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Houston',header=None).values.tolist()
#     master_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Masters')
#     master_players['Name']=master_players['Name'].str.title()
#     houston_merge=pd.merge(updated_groupby_factors,master_players,on='Name',how='right')
#     # st.write('Masters', houston_merge.sort_values(by='diff_last_3',ascending=False).reset_index(drop=True))
#     # st.write('masters', masters_2024.loc[:,['Name','position']])
#     final_masters_results=pd.merge(houston_merge,masters_2024.loc[:,['Name','position']],on='Name',how='left')
#     final_masters_results['combine_diffs']=final_masters_results['diff_last_3']+final_masters_results['diff_last_1']
#     st.write('Final Result',final_masters_results.loc[:,['Name','diff_last_3','diff_last_1','position','combine_diffs']])

# with st.expander('Hilton Head'):
#     # st.write('dtype',current_data_before_rank.dtypes)
#     pre_masters_data=current_data_before_rank[current_data_before_rank['Tournament']>-1]
#     pre_masters_data=pre_masters_data.drop('index',axis=1).sort_values(by=['Name','Tournament'],ascending=[True,True]).reset_index(drop=True)
#     pre_masters_data['event_tracker']=pre_masters_data.groupby('Name')['Tournament'].rank(method='first', ascending=True)

#     updated_groupby_factors=analysis_data(pre_masters_data).reset_index()
#     master_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Hilton_Head')
#     master_players['Name']=master_players['Name'].str.title()
#     houston_merge=pd.merge(updated_groupby_factors,master_players,on='Name',how='right').sort_values(by=['diff_last_3','diff_last_1'],ascending=[False,False])
#     # update below when results come in
#     final_masters_results=pd.merge(houston_merge,Hilton_Head_2024.loc[:,['Name','position']],on='Name',how='left').sort_values(by=['position','diff_last_3'],ascending=[True,False]).reset_index(drop=True)
#     # st.write('Final Result',final_masters_results.loc[:,['Name','diff_last_3','diff_last_1','position']].sort_values(by=['position'],ascending=[True]))

#     # st.write('Final Result',houston_merge.loc[:,['Name','diff_last_3','diff_last_1']].reset_index(drop=True))

#     hilton_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Hilton_Head_Betting')
#     hilton_players['Name']=hilton_players['Name'].str.title()
#     hilton_players['top_5_%']=1/hilton_players['Top_5']
#     hilton_players['top_10_%']=1/hilton_players['Top_10']
#     hilton_players['top_20_%']=1/hilton_players['Top_20']
#     hilton_players['top_30_%']=1/hilton_players['Top_30']
#     hilton_players['max_less_mins_10_not_top_5']=hilton_players[['top_10_%','top_20_%','top_30_%']].max(axis=1)-hilton_players[['top_10_%','top_20_%','top_30_%']].min(axis=1)
#     hilton_players['diff_to_fifty_fifty']=hilton_players[['top_10_%','top_20_%','top_30_%']].max(axis=1)-0.5
#     hilton_players['pos_by_tenth']=(hilton_players['diff_to_fifty_fifty'] / hilton_players['max_less_mins_10_not_top_5'])*10
#     hilton_selection=pd.merge(hilton_players,houston_merge,how='left',on='Name').sort_values(by=['diff_last_3','diff_last_1'],ascending=[False,False])
#     # st.write(Hilton_Head_2024)
#     hilton_selection=pd.merge(hilton_selection,Hilton_Head_2024.loc[:,['Name','position','AGG']],on='Name',how='left')
#     hilton_selection['agg_after_handicap'] = hilton_selection['AGG']-hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap'] = hilton_selection['agg_after_handicap'].rank(method='dense', ascending=True)

#     # hilton_selection['agg_after_handicap_ALT'] = hilton_selection['AGG']+hilton_selection['Handicap_Strokes']
#     # hilton_selection['POS_after_handicap_ALT'] = hilton_selection['agg_after_handicap_ALT'].rank(method='dense', ascending=True)


#     hilton_selection['cover_handicap?'] = np.where(hilton_selection['position']>=hilton_selection['Finishing_Position_2'],-1,1)
#     hilton_selection['combine_diffs']=hilton_selection['diff_last_3']+hilton_selection['diff_last_1']
#     hilton_head_results_betting=hilton_selection.loc[:,['Name','diff_last_3','diff_last_1','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True)
#     st.write('Betting Result', hilton_selection.loc[:,['Name','diff_last_3','diff_last_1','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True))
#     groupby_result_diff_3=hilton_selection.groupby(['diff_last_3']).agg(diff_3_result=('cover_handicap?','sum'),diff_3_count=('cover_handicap?','count'))
#     groupby_result_diff_1=hilton_selection.groupby(['diff_last_1']).agg(diff_1_result=('cover_handicap?','sum'),diff_1_count=('cover_handicap?','count'))
#     groupby_result_diff_comb=hilton_selection.groupby(['combine_diffs']).agg(diff_1_result=('cover_handicap?','sum'),diff_1_count=('cover_handicap?','count'))
#     st.write('groupby result diff 3',groupby_result_diff_3)
#     st.write('groupby result diff 1',groupby_result_diff_1)
#     st.write('groupby result diff combine',groupby_result_diff_comb)
#     st.write('Handicap Betting All Columns', hilton_selection.reset_index(drop=True))

    
# with st.expander('New Orleans'):
#     # st.write('dtype',current_data_before_rank.dtypes)
#     # pre_masters_data=current_data_before_rank[current_data_before_rank['Tournament']>-1]
#     # pre_masters_data=pre_masters_data.drop('index',axis=1).sort_values(by=['Name','Tournament'],ascending=[True,True]).reset_index(drop=True)
#     # pre_masters_data['event_tracker']=pre_masters_data.groupby('Name')['Tournament'].rank(method='first', ascending=True)

#     # updated_groupby_factors=analysis_data(pre_masters_data).reset_index()
#     # master_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Hilton_Head')
#     # master_players['Name']=master_players['Name'].str.title()
#     # houston_merge=pd.merge(updated_groupby_factors,master_players,on='Name',how='right').sort_values(by=['diff_last_3','diff_last_1'],ascending=[False,False])
#     # # update below when results come in
#     # final_masters_results=pd.merge(houston_merge,Hilton_Head_2024.loc[:,['Name','position']],on='Name',how='left').sort_values(by=['position','diff_last_3'],ascending=[True,False]).reset_index(drop=True)
#     # # st.write('Final Result',final_masters_results.loc[:,['Name','diff_last_3','diff_last_1','position']].sort_values(by=['position'],ascending=[True]))

#     # st.write('Final Result',houston_merge.loc[:,['Name','diff_last_3','diff_last_1']].reset_index(drop=True))

#     hilton_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Louisiana_Team_Betting')
#     hilton_players['Name']=hilton_players['Name'].str.title()
#     hilton_players['top_5_%']=1/hilton_players['Top_5']
#     hilton_players['top_10_%']=1/hilton_players['Top_10']
#     hilton_players['top_20_%']=1/hilton_players['Top_20']
#     hilton_players['top_30_%']=1/hilton_players['Top_30']
#     hilton_players['max_less_mins_10_not_top_5']=hilton_players[['top_10_%','top_20_%','top_30_%']].max(axis=1)-hilton_players[['top_10_%','top_20_%','top_30_%']].min(axis=1)
#     hilton_players['diff_to_fifty_fifty']=hilton_players[['top_10_%','top_20_%','top_30_%']].max(axis=1)-0.5
#     hilton_players['pos_by_tenth']=(hilton_players['diff_to_fifty_fifty'] / hilton_players['max_less_mins_10_not_top_5'])*10
#     hilton_selection=hilton_players.copy()
#     # st.write(Hilton_Head_2024)
#     # hilton_selection=pd.merge(hilton_selection,Hilton_Head_2024.loc[:,['Name','position','AGG']],on='Name',how='left')
#     hilton_selection['agg_after_handicap'] = hilton_selection['AGG']-hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap'] = hilton_selection['agg_after_handicap'].rank(method='dense', ascending=True)

#     hilton_selection['agg_after_handicap_ALT'] = hilton_selection['AGG']+hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap_ALT'] = hilton_selection['agg_after_handicap_ALT'].rank(method='dense', ascending=True)


#     hilton_selection['cover_handicap?'] = np.where(hilton_selection['position']>=hilton_selection['Finishing_Position_2'],-1,1)
#     st.write('Betting Result', hilton_selection.loc[:,['Name','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap','POS_after_handicap_ALT','agg_after_handicap_ALT']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True))


# with st.expander('Dallas'):

#     hilton_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Dallas_Betting')
#     hilton_players['Name']=hilton_players['Name'].str.title()
#     hilton_players['top_5_%']=1/hilton_players['Top_5']
#     hilton_players['top_10_%']=1/hilton_players['Top_10']
#     hilton_players['top_20_%']=1/hilton_players['Top_20']
#     hilton_players['top_30_%']=1/hilton_players['Top_30']
#     hilton_players['top_40_%']=1/hilton_players['Top_40']
#     hilton_players['max_less_mins_10_not_top_5']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].min(axis=1)
#     hilton_players['diff_to_fifty_fifty']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-0.5
#     hilton_players['pos_by_tenth']=(hilton_players['diff_to_fifty_fifty'] / hilton_players['max_less_mins_10_not_top_5'])*10
#     hilton_selection=hilton_players.copy()
#     # st.write(Hilton_Head_2024)
#     # st.write(dallas_2024)
#     st.write('Sungjae Im withdrew before Round 1')
#     st.write('A lot of top players covered the handicap something to keep in mind with weak players might be an angle')
#     hilton_selection=pd.merge(hilton_selection,dallas_2024.loc[:,['Name','position','AGG','MC']],on='Name',how='left')
#     hilton_selection['agg_after_handicap'] = (hilton_selection['AGG']*hilton_selection['MC'])-hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap'] = hilton_selection['agg_after_handicap'].rank(method='dense', ascending=True)

#     hilton_selection['cover_handicap?'] = np.where((hilton_selection['position']>=hilton_selection['Finishing_Position_2']),-1,1)
#     hilton_selection=hilton_selection[~hilton_selection['Name'].isin(['Sungjae Im'])]
#     # hilton_selection['combine_diffs']=hilton_selection['diff_last_3']+hilton_selection['diff_last_1']
#     st.write('Betting Result', hilton_selection.loc[:,['Name','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True))
#     # groupby_result_diff_3=hilton_selection.groupby(['diff_last_3']).agg(diff_3_result=('cover_handicap?','sum'),diff_3_count=('cover_handicap?','count'))
#     # groupby_result_diff_1=hilton_selection.groupby(['diff_last_1']).agg(diff_1_result=('cover_handicap?','sum'),diff_1_count=('cover_handicap?','count'))
#     # groupby_result_diff_comb=hilton_selection.groupby(['combine_diffs']).agg(diff_1_result=('cover_handicap?','sum'),diff_1_count=('cover_handicap?','count'))
#     # st.write('groupby result diff 3',groupby_result_diff_3)
#     # st.write('groupby result diff 1',groupby_result_diff_1)
#     # st.write('groupby result diff combine',groupby_result_diff_comb)
#     st.write('Handicap Betting All Columns', hilton_selection.reset_index(drop=True))

# with st.expander('Quail Hollow'):

#     hilton_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Charlotte_Betting')
#     hilton_players['Name']=hilton_players['Name'].str.title()
#     hilton_players['top_5_%']=1/hilton_players['Top_5']
#     hilton_players['top_10_%']=1/hilton_players['Top_10']
#     hilton_players['top_20_%']=1/hilton_players['Top_20']
#     hilton_players['top_30_%']=1/hilton_players['Top_30']
#     hilton_players['top_40_%']=1/hilton_players['Top_40']
#     hilton_players['max_less_mins_10_not_top_5']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].min(axis=1)
#     hilton_players['diff_to_fifty_fifty']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-0.5
#     hilton_players['pos_by_tenth']=(hilton_players['diff_to_fifty_fifty'] / hilton_players['max_less_mins_10_not_top_5'])*10
#     hilton_selection=hilton_players.copy()
#     # st.write(Hilton_Head_2024)
#     # st.write(dallas_2024)
#     # st.write('Sungjae Im withdrew before Round 1')
#     # st.write('A lot of top players covered the handicap something to keep in mind with weak players might be an angle')
#     hilton_selection=pd.merge(hilton_selection,quail_hollow_2024.loc[:,['Name','position','AGG','MC']],on='Name',how='left')
#     hilton_selection['agg_after_handicap'] = (hilton_selection['AGG']*hilton_selection['MC'])-hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap'] = hilton_selection['agg_after_handicap'].rank(method='dense', ascending=True)

#     hilton_selection['cover_handicap?'] = np.where((hilton_selection['position']>=hilton_selection['Finishing_Position_2']),-1,1)
#     # hilton_selection['position'].isna
#     hilton_selection=hilton_selection[~hilton_selection['position'].isna()]
#     hilton_selection=hilton_selection[~hilton_selection['Finishing_Position_1'].isna()]
#     # hilton_selection['combine_diffs']=hilton_selection['diff_last_3']+hilton_selection['diff_last_1']
#     st.write('Betting Result', hilton_selection.loc[:,['Name','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True))
#     st.write('Handicap Betting All Columns', hilton_selection.reset_index(drop=True))

# with st.expander('Valhalla'):

#     hilton_players=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Valhalla_Betting')
#     hilton_players['Name']=hilton_players['Name'].str.title()
#     hilton_players['top_5_%']=1/hilton_players['Top_5']
#     hilton_players['top_10_%']=1/hilton_players['Top_10']
#     hilton_players['top_20_%']=1/hilton_players['Top_20']
#     hilton_players['top_30_%']=1/hilton_players['Top_30']
#     hilton_players['top_40_%']=1/hilton_players['Top_40']
#     hilton_players['max_less_mins_10_not_top_5']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].min(axis=1)
#     hilton_players['diff_to_fifty_fifty']=hilton_players[['top_10_%','top_20_%','top_30_%','top_40_%']].max(axis=1)-0.5
#     hilton_players['pos_by_tenth']=(hilton_players['diff_to_fifty_fifty'] / hilton_players['max_less_mins_10_not_top_5'])*10
#     hilton_selection=hilton_players.copy()
#     st.write(valhalla_2024)
#     # st.write(dallas_2024)
#     # st.write('Sungjae Im withdrew before Round 1')
#     # st.write('A lot of top players covered the handicap something to keep in mind with weak players might be an angle')
#     hilton_selection=pd.merge(hilton_selection,valhalla_2024.loc[:,['Name','position','AGG','MC']],on='Name',how='left')
#     hilton_selection['agg_after_handicap'] = (hilton_selection['AGG']*hilton_selection['MC'])-hilton_selection['Handicap_Strokes']
#     hilton_selection['POS_after_handicap'] = hilton_selection['agg_after_handicap'].rank(method='dense', ascending=True)

#     hilton_selection['cover_handicap?'] = np.where((hilton_selection['position']>=hilton_selection['Finishing_Position_2']),-1,1)
#     # hilton_selection['position'].isna
#     hilton_selection=hilton_selection[~hilton_selection['position'].isna()]
#     hilton_selection=hilton_selection[~hilton_selection['Finishing_Position_1'].isna()]
#     # hilton_selection['combine_diffs']=hilton_selection['diff_last_3']+hilton_selection['diff_last_1']
#     st.write('Betting Result', hilton_selection.loc[:,['Name','POS_after_handicap','position','Finishing_Position_1',
#     'cover_handicap?','Handicap_Strokes','agg_after_handicap']]\
#              .sort_values(by=['POS_after_handicap']).reset_index(drop=True))
#     st.write('Handicap Betting All Columns', hilton_selection.reset_index(drop=True))


with st.expander('All Betting Analysis'):

    df_betting_raw=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='betting_data',
                                 date_parser=lambda x: pd.to_datetime(x, format='%m/%d/%Y'),
                                #  converters= {'date': pd.to_datetime}
                                 )
    
    # st.write(combined_data[combined_data['Name'].str.contains('ory')])
    df_betting_raw['Name']=df_betting_raw['Name'].str.title()
    # st.write(df_betting_raw[df_betting_raw['Name'].str.contains('ory')])
    # st.write('hawaii 2025', hawaii_2025)
    # st.write('hawaii date',hawaii_2025['date'][0].strftime('%B %d, %Y'))
    # issue with date time of 12 Jan on betting versus OGWR, need to fix 
    # filter on hawaii in 2025
    # how to make sure that the dates are american dates and not european dates
    # st.write('betting raw', df_betting_raw[(df_betting_raw['year']==2025) & (df_betting_raw['Tour_Name']=='hawaii')].sort_values(by='date'))
    hawaii_test_df=df_betting_raw[(df_betting_raw['year']==2025) & (df_betting_raw['Tour_Name']=='hawaii')].sort_values(by='date')
    # st.write('betting odds spreadsheet date',hawaii_test_df['date'][0].strftime('%B %d, %Y'))
    # extract the month from date column
    # st.write(hawaii_test_df['date'].dt.month)
    df_betting_results=pd.merge(df_betting_raw,combined_data,on=['date','Name'],how='left',indicator=True)
    # st.write('Change the ISCO to 13 July')
    # full_df.loc [ (full_df['full_name']=='heung-min_son'), 'full_name' ]
    df_betting_results.loc[(df_betting_results['Tour_Name']=='isco_kentucky'),'date']=pd.to_datetime('13-07-2024',dayfirst=True)
    df_betting_results.loc[(df_betting_results['Tour_Name']=='barracuda'),'date']=pd.to_datetime('20-07-2024',dayfirst=True)
    # st.write('tour name',df_betting_results['Tour_Name'].unique())
    df_betting_results.loc[(df_betting_results['Tour_Name']=='dubai_desert'),'date']=pd.to_datetime('18-01-2025',dayfirst=True)    
    # st.write(df_betting_results.loc['date','Event Name'])
    df_betting_results.to_parquet('C:/Users/Darragh/Documents/Python/Golf/golf_odds_results_combined.parq')
    st.write('Check the indicator to see if anything missing after merge',df_betting_results[df_betting_results['_merge'].str.contains('left')].sort_values(by='date'))
    df_betting_results=df_betting_results[~df_betting_results['position'].isna()]
    df_betting_results=df_betting_results.sort_values(by=['date','Winner_odds'],ascending=[False,True])

    # in_handicap_betting=df_betting_results['Handicap_Payout']>1
    df_betting_results['in_handicap_betting']=np.where(df_betting_results['Handicap_Payout']>1,1,np.NaN)
    df_betting_results['agg_after_handicap'] = (df_betting_results['AGG']*df_betting_results['MC'])-df_betting_results['Handicap_Strokes']
    
    # df_betting_results['agg_after_handicap']=df_betting_results['agg_after_handicap'].where(df_betting_results['Handicap_Payout']>1)

    df_betting_results['POS_after_handicap'] = df_betting_results.groupby('Tour_Name')['agg_after_handicap'].rank(method='dense', ascending=True)
    df_betting_results['POS_after_handicap']=np.where((df_betting_results['in_handicap_betting']==1)&(df_betting_results['miss_cut']==1),16,df_betting_results['POS_after_handicap'])

    # df_betting_results['POS_after_handicap']=np.where(df_betting_results['Handicap_Payout']>1,df_betting_results['POS_after_handicap'],16)
    # st.write('Checking Handicap betting',df_betting_results[df_betting_results['Name'].str.contains('Wyn')])
    df_betting_results['cover_handicap?'] = np.where((df_betting_results['position']>=df_betting_results['Finishing_Position_2']),-1,1)
    df_betting_results['alt_pos'] = df_betting_results['position'].where(df_betting_results['position'] != 999, 80)
    df_betting_results['surplus_pos_result'] = df_betting_results['Finishing_Position_1'] - df_betting_results['alt_pos']
    df_betting_results['momentum_pick']=np.where(df_betting_results['Open_Winner_odds']==df_betting_results['Winner_odds'],0,np.where(
    df_betting_results['Winner_odds']<df_betting_results['Open_Winner_odds'],1,-1))
    cols_to_move=['Tour_Name','date','Name','Finishing_Position_1','Finish Pos.','cover_handicap?','surplus_pos_result','agg_after_handicap']
    cols = cols_to_move + [col for col in df_betting_results if col not in cols_to_move]
    df_betting_results=df_betting_results[cols].sort_values(by=['date','Name'],ascending=True)
    # st.write('after merge', df_betting_results)
    # st.write('Last result',df_betting_results.drop_duplicates(subset='Name',keep='first'))
    # results_by_name = df_betting_results.groupby('Name').agg(surplus_position=('surplus_pos_result','sum'),
    #                                                          count_tourn=('surplus_pos_result','count'),cover_result=('cover_handicap?','sum')).reset_index()
    # st.write(combined_data.head())
    st.write(combined_data.groupby('Event Name').agg(count_players=('AGG','count')))
    # st.write('Cover Results Worst Performers:', results_by_name.sort_values(by='cover_result',ascending=True))
    # st.write('Cover Results Best Performers:', results_by_name.sort_values(by=['cover_result'],ascending=[False]))
    # st.write('Surplus Position Results:', results_by_name.sort_values(by='surplus_position',ascending=False))

    # st.write('Canada:', df_betting_results[df_betting_results['Tour_Name']=='canada'].sort_values(by=['agg_after_handicap','position'],ascending=[True,True]))
    # st.write('Colonial:', df_betting_results[df_betting_results['Tour_Name']=='Colonial'].sort_values(by=['agg_after_handicap','position'],ascending=[True,True]))
    # st.write('Valhalla:', df_betting_results[df_betting_results['Tour_Name']=='Valhalla'].sort_values(by=['agg_after_handicap','position'],ascending=[True,True]))

with st.expander('Momentum'):
    momentum_results = df_betting_results.groupby('momentum_pick').agg(mom_results=('cover_handicap?','sum'),count=('cover_handicap?','count'))
    st.write(momentum_results)
    momentum_results_event = df_betting_results.groupby(['date','Tour_Name','momentum_pick']).agg(cover_handicap=('cover_handicap?','sum'),count=('cover_handicap?','count')).reset_index().sort_values(by=['date'],ascending=False)
    # st.write(momentum_results_event)
    summary_momentum_results_event=momentum_results_event[momentum_results_event['momentum_pick']!=0]
    st.write(summary_momentum_results_event)
    def graph_pl(summary_momentum_results_event,column):
        line_cover= alt.Chart(summary_momentum_results_event).mark_line().encode(alt.X('date:T',axis=alt.Axis(title='Week',labelAngle=0)),
        alt.Y(column),color=alt.Color('momentum_pick:N'))
        text_cover=line_cover.mark_text(baseline='middle',dx=0,dy=-15).encode(text=alt.Text(column),color=alt.value('black'))
        overlay = pd.DataFrame({column: [0]})
        vline = alt.Chart(overlay).mark_rule(color='black', strokeWidth=1).encode(y=column)
        return st.altair_chart(line_cover + text_cover + vline,use_container_width=True)

    graph_pl(summary_momentum_results_event,column='cover_handicap')    
    # st.altair_chart(alt.Chart(summary_momentum_results_event).mark_line().encode(x='date:T',y='cover_handicap:Q',color='momentum_pick:N'),use_container_width=True)
    # factor_bets = (analysis_factors[analysis_factors['bet_sign']!=0]).copy()
    
    # momentum_results_event = df_betting_results.groupby(['date','Tour_Name','momentum_pick'])['cover_handicap?'].sum().reset_index().sort_values(by='date')
    # mom_pivot=pd.pivot_table(df_betting_results,values=['cover_handicap?'],index=['momentum_pick'],columns=['date'],aggfunc='sum').reset_index()
    # st.write(df_betting_results.dtypes)
    
    st.write(df_betting_results.groupby(['momentum_pick','cover_handicap?']).agg(mom_results=('cover_handicap?','sum'),count=('cover_handicap?','count')))
    
    # st.write(mom_pivot)

with st.expander('Season Cover Factor'):
    # st.write(df_betting_results)
    x=df_betting_results.groupby (['Name'])['cover_handicap?'].apply(lambda x: x.cumsum().shift()).reset_index().rename(columns={'level_1':'unique_id'}).rename(columns={'cover_handicap?':'season_cover'})

    y=df_betting_results.reset_index().rename(columns={'index':'unique_id'})
    season_cover_df=pd.merge(x,y,how='outer',on=['unique_id','Name']).rename(columns={'season_cover':'season_cover_prev'})
    # st.write('after merge', season_cover_df)
    season_cover_df=season_cover_df.reset_index().sort_values(by=['date','Name'],ascending=True).drop(['index','unique_id'],axis=1)
    season_cover_df['season_cover_prev_sign']=np.sign(season_cover_df['season_cover_prev'])
    # st.write(season_cover_df)

    momentum_results = season_cover_df.groupby('season_cover_prev_sign').agg(season_cover_results=('cover_handicap?','sum'),count=('cover_handicap?','count'))
    st.write(momentum_results)
    momentum_results_event = season_cover_df.groupby(['date','Tour_Name','season_cover_prev_sign']).agg(cover_handicap=('cover_handicap?','sum'),count=('cover_handicap?','count')).reset_index().sort_values(by=['date'],ascending=False)
    # st.write(momentum_results_event)
    summary_momentum_results_event=momentum_results_event[momentum_results_event['season_cover_prev_sign']!=0]
    st.write(summary_momentum_results_event)
    def graph_pl(summary_momentum_results_event,column):
        line_cover= alt.Chart(summary_momentum_results_event).mark_line().encode(alt.X('date:T',axis=alt.Axis(title='Week',labelAngle=0)),
        alt.Y(column),color=alt.Color('season_cover_prev_sign:N'))
        text_cover=line_cover.mark_text(baseline='middle',dx=0,dy=-15).encode(text=alt.Text(column),color=alt.value('black'))
        overlay = pd.DataFrame({column: [0]})
        vline = alt.Chart(overlay).mark_rule(color='black', strokeWidth=1).encode(y=column)
        return st.altair_chart(line_cover + text_cover + vline,use_container_width=True)

    graph_pl(summary_momentum_results_event,column='cover_handicap')    
    # st.altair_chart(alt.Chart(summary_momentum_results_event).mark_line().encode(x='date:T',y='cover_handicap:Q',color='momentum_pick:N'),use_container_width=True)
    # factor_bets = (analysis_factors[analysis_factors['bet_sign']!=0]).copy()
    
    # momentum_results_event = df_betting_results.groupby(['date','Tour_Name','momentum_pick'])['cover_handicap?'].sum().reset_index().sort_values(by='date')
    # mom_pivot=pd.pivot_table(df_betting_results,values=['cover_handicap?'],index=['momentum_pick'],columns=['date'],aggfunc='sum').reset_index()
    # st.write(df_betting_results.dtypes)
    
    st.write(season_cover_df.groupby(['season_cover_prev_sign','cover_handicap?']).agg(season_cover_results=('cover_handicap?','sum'),count=('cover_handicap?','count')))    
    
    # st.write(season_cover_df[(season_cover_df['Tour_Name']=='memorial') & (season_cover_df['season_cover_prev_sign']==-1) ])
# with st.expander('Canada'):

#     canada_entrants=pd.read_excel('C:/Users/Darragh/Documents/Python/golf/golf_masters_historical.xlsx',sheet_name='Canada',header=[0])
#     canada_entrants['Name']=canada_entrants['Name'].str.title()
#     # st.write(canada_entrants)
#     # st.write(df_betting_results[df_betting_results['Name'].str.contains('eith')])
#     st.write(combined_data[combined_data['Name'].str.contains('itche')])
#     canada=pd.merge(df_betting_results,canada_entrants,on='Name',how='right').sort_values(by=['date','Winner_odds'],ascending=[False,True])
#     cols_to_move=['Tour_Name','date','Name','Finishing_Position_1','Finish Pos.','cover_handicap?']
#     cols = cols_to_move + [col for col in canada if col not in cols_to_move]
#     canada=canada[cols]
#     st.write(canada.drop_duplicates(subset='Name',keep='first'))
#     canada_update=pd.merge(results_by_name,canada_entrants,on='Name',how='right')
#     st.write(canada_update.sort_values(by='surplus_position',ascending=False))




with st.expander('Season to Date Cover Graph'):
    # df_stdc_1=canada.loc[:,['date','Name','cover_handicap?']].copy()
    df_stdc_1=df_betting_results.loc[:,['date','Name','cover_handicap?','surplus_pos_result']].copy()
    df_2025=df_stdc_1.loc[df_stdc_1['date']>'01-01-25']
    # st.write('is there duplicate index',df_stdc_1)
    # st.write( df_stdc_1[df_stdc_1.index.duplicated()] )
    # st.write( df_stdc_1[df_stdc_1.duplicated()] )
    # st.write(pd.pivot_table(df_stdc_1,values=['cover_handicap?'],index=['Name'],columns=['date']))
    def pivot_generation(df_stdc_1,col_selection='cover_handicap?'):
        test_pivot=pd.pivot(df_stdc_1,values=[col_selection],index=['Name'],columns=['date']).reset_index()
        test_pivot.columns = test_pivot.columns.get_level_values(1)
        test_pivot=test_pivot.set_index('NaT')
        test_pivot.index.names=['Name']
        test_pivot['total_cover']=test_pivot.sum(axis=1)
        return test_pivot
    test_pivot=pivot_generation(df_stdc_1,col_selection='cover_handicap?')
    test_pivot_1=pivot_generation(df_stdc_1,col_selection='surplus_pos_result')
    test_pivot_2025=pivot_generation(df_2025,col_selection='cover_handicap?')
    test_pivot_1_2025=pivot_generation(df_2025,col_selection='surplus_pos_result')

    # st.write(test_pivot.columns)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
    def highlight_max(cell):   # sourcery skip: assign-if-exp
        if cell > 0 : 
            return 'background-color:green'
        if cell < 0 : 
            return 'background-color:red'
        else: 
            return ''
  
    # st.write(test_pivot.sort_values(by=['total_cover'],ascending=False).style.applymap(highlight_max))

    st.write(test_pivot_2025.sort_values(by=['total_cover'],ascending=False).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot_1_2025.sort_values(by=['total_cover'],ascending=False).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot_2025.sort_values(by=['total_cover'],ascending=True).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot_1_2025.sort_values(by=['total_cover'],ascending=True).style.format(precision=0).applymap(highlight_max))



    st.write(test_pivot.sort_values(by=['total_cover'],ascending=False).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot_1.sort_values(by=['total_cover'],ascending=False).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot.sort_values(by=['total_cover'],ascending=True).style.format(precision=0).applymap(highlight_max))
    st.write(test_pivot_1.sort_values(by=['total_cover'],ascending=True).style.format(precision=0).applymap(highlight_max))


    # st.write('Filter by specific name', test_pivot.loc[['Davis Thompson','Sam Burns'],:]) # this works
    # st.write('Filter by partial name', test_pivot.loc[test_pivot.index.str.contains('Burns|Spieth'),:]) #this works and i prefer it
    # st.write(test_pivot.loc[test_pivot.index.str.contains('Burns|Spieth'),:].sort_values(by=['total_cover'],ascending=False).style.format(precision=0).applymap(highlight_max))

    # st.write(test_pivot.sort_values(by=['total_cover'],ascending=False))
    df_stdc_1['average']=df_stdc_1.groupby('Name')['cover_handicap?'].transform(np.mean)
    chart_cover= alt.Chart(df_stdc_1).mark_rect().encode(alt.X('date:N',axis=alt.Axis(title='date',labelAngle=0)),
    alt.Y('Name',sort=alt.SortField(field='average', order='descending')),color=alt.Color('cover_handicap?:Q',scale=alt.Scale(scheme='redyellowgreen')))
    # https://altair-viz.github.io/gallery/layered_heatmap_text.html
    # https://vega.github.io/vega/docs/schemes/
    text_cover=chart_cover.mark_text().encode(text=alt.Text('cover_handicap?:N'),color=alt.value('black'))
    # st.altair_chart(chart_cover + text_cover,use_container_width=True)

with st.expander('Handicap Results Graph'):
    # df_stdc_1=canada.loc[:,['date','Name','cover_handicap?']].copy()
    df_stdc_1=df_betting_results.loc[:,['date','Name','cover_handicap?','POS_after_handicap']].copy()
    df_2025=df_stdc_1.loc[df_stdc_1['date']>'01-01-25']
    def run_code_1(df_stdc_1):
        # st.write(df_stdc_1[df_stdc_1['date']>'06-05-24'])
        df_stdc_1=df_stdc_1.dropna(subset=['POS_after_handicap'])
        
        
        test_pivot=pivot_generation(df_stdc_1,col_selection='POS_after_handicap')

        # st.write(test_pivot.sort_values(by=['total_cover'],ascending=True).style.format(precision=0).background_gradient(axis=0, cmap='bwr')) #bwr
        # https://matplotlib.org/stable/users/explain/colors/colormaps.html

        test_pivot=test_pivot.drop('total_cover',axis=1)
        return test_pivot
    
    test_pivot=run_code_1(df_stdc_1)
    test_pivot_2025=run_code_1(df_2025)
    # st.write('df 2025', df_2025)
    # st.write('test piv', test_pivot_2025)
    # st.write('betting',df_betting_results.loc[df_betting_results['date']>'01-01-25'])
    count_players=test_pivot.copy()
    def run_code_2(test_pivot,df_betting_results):
        
        date_event=df_betting_results.loc[:,['Tour_Name','date']].drop_duplicates().reset_index(drop=True)
        # st.write('date event', date_event)
        cols = list(zip(date_event['date'], date_event['Tour_Name']))
        # st.write
        test_pivot.columns = pd.MultiIndex.from_tuples(cols)
        test_pivot['top_3']=test_pivot.isin({1,2,3}).sum(axis=1)
        
        # st.write(test_pivot.sort_values(by=['top_3'],ascending=False).style.format(precision=0).background_gradient(axis=0, cmap='bwr')) #bwr
        # https://matplotlib.org/stable/gallery/color/named_colors.html
        def highlight_custom(cell):   # sourcery skip: assign-if-exp
            if cell ==1: 
                return 'background-color:lime'
            if cell == 2 : 
                return 'background-color:green'
            if cell == 3 : 
                return 'background-color:green'
            if cell > 3 : 
                return 'background-color:lightgrey'
            else: 
                return ''
            


        return st.write(test_pivot.sort_values(by=['top_3'],ascending=False).style.format(precision=0).applymap(highlight_custom)) 
    
    run_code_2(test_pivot_2025,df_betting_results.loc[df_betting_results['date']>'01-01-25'])
    run_code_2(test_pivot,df_betting_results)
    # betting_2025_data=df_betting_results.loc[df_betting_results['date']>'01-01-25']
    # # st.write('filtered 2025', betting_2025_data)
    # date_event=betting_2025_data.loc[:,['Tour_Name','date']].drop_duplicates().reset_index(drop=True)
    # # st.write('date event 2025', date_event)
    # cols = list(zip(date_event['date'], date_event['Tour_Name']))
    # # st.write('cols of 2025', cols)
    # st.write('test pivot before error', test_pivot_2025)
    # # test_pivot_2025.columns = pd.MultiIndex.from_tuples(cols)
    # st.write('test pivot', test_pivot_2025)

with st.expander('Power Ranking'):
    # https://stackoverflow.com/questions/37364859/pandas-add-header-row-for-multiindex
    # https://github.com/streamlit/streamlit/issues/6319

    date_event=df_betting_results.loc[:,['Tour_Name','date']].drop_duplicates().reset_index(drop=True)
    cols = list(zip(date_event['date'], date_event['Tour_Name']))
    # st.write(date_event)
    count_players.columns = pd.MultiIndex.from_tuples(cols)
    count_players['total']=count_players.count(axis=1)
    count_players=count_players.sort_values(by='total',ascending=False)
    # st.write(count_players.reset_index())
    count_players_min_3=count_players[count_players['total']>2]
    # st.write(count_players_min_3.columns)
    # count_players_min_3.columns = pd.MultiIndex.from_tuples(cols)
    st.write(count_players_min_3.reset_index())

    handicap_df=df_betting_results.loc[:,['date','Name','Handicap_Strokes_Adj','Tour_Name']].copy()
    handicap_df=handicap_df[handicap_df['Handicap_Strokes_Adj'].notna()].copy().sort_values(by=['date','Handicap_Strokes_Adj']).reset_index(drop=True)
    
    # exclude Dallas Colonial Canada as just not enough players to compare against
    # handicap_df=handicap_df[handicap_df['Tour_Name']!='Dallas'].copy()
    handicap_df=handicap_df[~handicap_df['Tour_Name'].isin({'Dallas','canada','Colonial','detroit'})].copy()
    # https://stackoverflow.com/questions/41594703/pandas-assign-an-index-to-each-group-identified-by-groupby
    handicap_df['week'] = handicap_df.groupby(['Tour_Name']).ngroup()-3
    handicap_df['count']=handicap_df.groupby('Name')['Handicap_Strokes_Adj'].transform('count')
    # st.write(handicap_df)
    handicap_df=handicap_df[handicap_df['count']>3].reset_index(drop=True).set_index('date')
    handicap_df['count_players']=handicap_df.groupby('week')['Handicap_Strokes_Adj'].transform('count')
    st.write(handicap_df)
    st.write(handicap_df.groupby('Name')['week'].count().reset_index().sort_values(by='week',ascending=False).reset_index(drop=True))

    df_data=handicap_df.loc[:,['Name','week','Handicap_Strokes_Adj']].rename(columns={'Handicap_Strokes_Adj':'adj_spread','Name':'ID','week':'Week'}).reset_index(drop=True)
    # st.write('df', df_data)
    
    result_data = []

    for week in df_data['Week'].unique():
        week_data = df_data[df_data['Week'] == week]
        players = week_data['ID'].tolist()
        handicaps = week_data['adj_spread'].tolist()
        
        for i, j in product(range(len(players)), repeat=2):
            if i != j:
                result_data.append({
                    'ID': players[i],
                    'Opponent': players[j],
                    'Week': week,
                    'adj_spread': handicaps[i] - handicaps[j]
                })
                # st.write('week_data', week_data)
                # st.write('i:',i,'j:',j)
                # st.write('results',pd.DataFrame(result_data))


    # Create the resulting DataFrame
    df_result_data_1 = pd.DataFrame(result_data)
    # st.write(df_result_data_1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    df_data=pd.DataFrame({'Name':['Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm',],'Week':[-3,-3,-3,-2,-2,-2,-1,-1,-1,0,0,0,1,1,1,2,2,2,3,3,3],
                          'Handicap':[0,3,2,0,4,4,0,2,2,0,1,1,0,2,3,0,1,4,0,3,4]})
    
    # df_data=pd.DataFrame({'Name':[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2],'Week':[-3,-3,-3,-2,-2,-2,-1,-1,-1,0,0,0,1,1,1,2,2,2,3,3,3],
    #                       'Handicap':[0,3,2,0,4,4,0,2,2,0,1,1,0,2,3,0,1,4,0,3,4]})


    result_data_product = []

    for week in df_data['Week'].unique():
        week_data = df_data[df_data['Week'] == week]
        players = week_data['Name'].tolist()
        handicaps = week_data['Handicap'].tolist()
        
        for i, j in product(range(len(players)), repeat=2):
            if i != j:
                result_data_product.append({
                    'Name': players[i],
                    'Opponent': players[j],
                    'Week': week,
                    'Handicap': handicaps[i] - handicaps[j]
                })

    df_result_data_product = pd.DataFrame(result_data_product)




    result_data = []

    # Determine relevant combinations dynamically
    for week in df_data['Week'].unique():
        week_data = df_data[df_data['Week'] == week].reset_index(drop=True)
        
        for i, j in combinations(range(len(week_data)), 2):
            name_i, name_j = week_data.loc[i, 'Name'], week_data.loc[j, 'Name']
            handicap_i, handicap_j = week_data.loc[i, 'Handicap'], week_data.loc[j, 'Handicap']
            
            # Determine relevant pairs based on unique combinations
            if name_i != name_j:
                result_data.append({
                    'Name': name_i,
                    'Opponent': name_j,
                    'Week': week,
                    'Handicap': handicap_i - handicap_j
                })
                # result_data.append({
                #     'Name': name_j,
                #     'Opponent': name_i,
                #     'Week': week,
                #     'Handicap': handicap_j - handicap_i
                # })

    # Create the resulting DataFrame
    df_result_data = pd.DataFrame(result_data).drop_duplicates(subset=['Name', 'Opponent', 'Week', 'Handicap'])

    # Sort and reset index to match the expected format
    df_result_data = df_result_data.sort_values(by=['Week', 'Name', 'Opponent']).reset_index(drop=True).rename(columns={'Name':'Home ID', 'Opponent':'Away ID'})
    # st.write('product data is working', df_result_data_product)
    df_result_data_product=df_result_data_product.drop('Opponent',axis=1).reset_index(drop=True).rename(columns={'Name':'ID'})

    # st.write('product data', df_result_data_product)
    # st.write('chat gpt result',df_result_data.sort_values(by=['Home ID','Week','Away ID']))
    df_result_data_product['adj_spread']=df_result_data_product['Handicap'].rolling(window=4, center=False).apply(lambda x: np.sum((np.array([0.125, 0.25,0.5,1]))*x), raw=False)
    # st.write('result data', df_result_data)
    power_df = df_result_data_product.groupby(['Week','ID'])['adj_spread'].sum().reset_index()
    # st.write('after power df', power_df)
    # st.write('sum of above handicaps', df_result_data['Handicap'].sum())

    games_df=df_result_data.copy()
    # st.write('games df', games_df)
    last_week=3
    first=list(range(-3,last_week-3))
# sourcery skip: remove-zero-from-range
    last=list(range(0,last_week))
    number_of_teams=df_result_data_product['ID'].nunique()
    # st.write('teams', number_of_teams)

    def test_4(matrix_df_1):
        weights = np.array([0.125, 0.25,0.5,1])
        sum_weights = np.sum(weights)
        matrix_df_1['adj_spread']=matrix_df_1['spread_with_home_adv'].rolling(window=4, center=False).apply(lambda x: np.sum(weights*x), raw=False)
        return matrix_df_1



    # df_result_data=pd.DataFrame({'Home ID':['Scottie','Scottie','Rory','Scottie','Scottie','Rory','Scottie','Scottie','Rory'],
    #                              'Away ID':['Rory','Rahm','Rahm','Rory','Rahm','Rahm','Rory','Rahm','Rahm'],
    #                              'Week':[1,1,1,2,2,2,3,3,3],
    #                       'Handicap':[-2,-3,-1,-1,-4,-3,-3,-4,-1]})
    # games_df=df_result_data.copy()

    def games_matrix_workings(first_4):
        group_week = first_4.groupby('Week')
        raw_data_2=[]
        game_weights = iter([-0.125, -0.25,-0.5,-1])
        for name, group in group_week:
            group['game_adj']=next(game_weights)
            # st.write('looking at for loop',group)
            raw_data_2.append(group)

        df3 = pd.concat(raw_data_2, ignore_index=True)
        # st.write('df3', df3)
        adj_df3=df3.loc[:,['Home ID', 'Away ID', 'game_adj']].copy()
        test_adj_df3 = adj_df3.rename(columns={'Home ID':'Away ID', 'Away ID':'Home ID'})
        concat_df_test=pd.concat([adj_df3,test_adj_df3]).sort_values(by=['Home ID', 'game_adj'],ascending=[True,False])
        test_concat_df_test=concat_df_test.groupby('Home ID')['game_adj'].sum().abs().reset_index()
        test_concat_df_test['Away ID']=test_concat_df_test['Home ID']
        # st.write('concat df test',concat_df_test,'test concat df test', test_concat_df_test)
        full=pd.concat([concat_df_test,test_concat_df_test]).sort_values(by=['Home ID', 'game_adj'],ascending=[True,False])
        # st.write('after concat', full)
        full_stack=pd.pivot_table(full,index='Away ID', columns='Home ID',aggfunc='sum')
        # st.write('Check sum looks good all zero', full_stack.sum())
        # st.write('Check sum looks good all zero', full_stack)
        full_stack=full_stack.fillna(0)
        full_stack.columns = full_stack.columns.droplevel(0)
        return full_stack

    # st.write('dont think i need the below as its in the function below but good to sense check')
    # st.write(games_matrix_workings(games_df[games_df['Week'].between(-3,0)]))
    power_ranking=[]
    for first,last in zip(first,last):
        first_section=games_df[games_df['Week'].between(first,last)]
        # st.write('first section', first_section)
        full_game_matrix=games_matrix_workings(first_section)
        # st.write('full game matrix', full_game_matrix)
        # st.write('full game matrix indexer', full_game_matrix.iloc[0:2,0:2])
        adjusted_matrix=full_game_matrix.iloc[:-1,:-1] # drop last column and last row of the Adjusted Games Played Matrix
        # st.write('adjusted matrix', adjusted_matrix)
        df_inv = pd.DataFrame(np.linalg.pinv(adjusted_matrix.values), adjusted_matrix.columns, adjusted_matrix.index)
        # st.write('df inv', df_inv)
        power_df_week=power_df[power_df['Week']==last].drop_duplicates(subset=['ID'],keep='last').set_index('ID')\
        .drop('Week',axis=1).rename(columns={'adj_spread':0}).iloc[:-1,:]
        # st.write('power_df_week', power_df_week,'first', first, 'last', last)
        result = df_inv.dot(pd.DataFrame(power_df_week))
        # st.write('result', result)
        result.columns=['power']
        avg=(result['power'].sum())/number_of_teams
        result['avg_pwr_rank']=(result['power'].sum())/number_of_teams
        result['final_power']=result['avg_pwr_rank']-result['power']
        df_pwr=pd.DataFrame(columns=['final_power'],data=[avg])
        result=pd.concat([result,df_pwr],ignore_index=True)
        result['week']=last+1
        power_ranking.append(result)
    power_ranking_combined = pd.concat(power_ranking).reset_index().rename(columns={'index':'ID'})
    st.write('Final Result of Spread', power_ranking_combined)



    
    # below is small code and sense checked
    df_data=pd.DataFrame({'Name':['Scottie','Rory','Rahm','Scottie','Rory','Rahm','Scottie','Rory','Rahm',],'Week':[1,1,1,2,2,2,3,3,3],
                          'Handicap':[0,2,3,0,1,4,0,3,4]})


    df_result_data=pd.DataFrame({'Name':['Scottie','Scottie','Rory','Scottie','Scottie','Rory','Scottie','Scottie','Rory'],
                                 'Opponent':['Rory','Rahm','Rahm','Rory','Rahm','Rahm','Rory','Rahm','Rahm'],
                                 'Week':[1,1,1,2,2,2,3,3,3],
                          'Handicap':[-2,-3,-1,-1,-4,-3,-3,-4,-1]})

    st.write('check result', df_result_data.sort_values(by=['Week', 'Name', 'Opponent']).reset_index(drop=True))

    result_data = []

    # Determine relevant combinations dynamically
    for week in df_data['Week'].unique():
        week_data = df_data[df_data['Week'] == week].reset_index(drop=True)
        
        for i, j in combinations(range(len(week_data)), 2):
            name_i, name_j = week_data.loc[i, 'Name'], week_data.loc[j, 'Name']
            handicap_i, handicap_j = week_data.loc[i, 'Handicap'], week_data.loc[j, 'Handicap']
            
            # Determine relevant pairs based on unique combinations
            if name_i != name_j:
                result_data.append({
                    'Name': name_i,
                    'Opponent': name_j,
                    'Week': week,
                    'Handicap': handicap_i - handicap_j
                })
                # result_data.append({
                #     'Name': name_j,
                #     'Opponent': name_i,
                #     'Week': week,
                #     'Handicap': handicap_j - handicap_i
                # })

    # Create the resulting DataFrame
    df_result_data = pd.DataFrame(result_data).drop_duplicates(subset=['Name', 'Opponent', 'Week', 'Handicap'])

    # Sort and reset index to match the expected format
    df_result_data = df_result_data.sort_values(by=['Week', 'Name', 'Opponent']).reset_index(drop=True)

    st.write('chat gpt result',df_result_data)    
    # df_result_data=pd.DataFrame({'Name':['Scottie','Scottie','Scottie','Scottie','Scottie','Scottie','Rory','Rory','Rory','Rory','Rory','Rory','Rahm','Rahm','Rahm','Rahm','Rahm','Rahm'],
    #                              'Opponent':['Rory','Rahm','Rory','Rahm','Rory','Rahm','Scottie','Rahm','Scottie','Rahm','Scottie','Rahm','Scottie','Rory','Scottie','Rory','Scottie','Rory'],
    #                              'Week':[1,1,2,2,3,3,1,1,2,2,3,3,1,1,2,2,3,3],
    #                       'Handicap':[-2,-3,-1,-4,-3,-4,2,-1,1,-3,3,-1,3,1,4,3,4,1]})


with st.expander('Data PGA Tour SG'):
    hilton_head_sg_approach=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/hilton_head_app.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_app'})
    hilton_head_ott=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/hilton_head_ott.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_ott'})
    hilton_head_arg=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/hilton_head_arg.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_arg'})
    hilton_head_putting=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/hilton_head_putting.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_putt'})
    # hilton_head_sg=pd.concat([hilton_head_sg_approach,hilton_head_ott,hilton_head_arg,hilton_head_putting],axis=0)
    hilton_head_sg=pd.merge(hilton_head_sg_approach,hilton_head_ott,how='outer')
    hilton_head_sg=pd.merge(hilton_head_sg,hilton_head_arg,how='outer')
    hilton_head_sg=pd.merge(hilton_head_sg,hilton_head_putting,how='outer')
    hilton_head_sg['Tournament']='hilton_head'
    hilton_head_sg['Date']=pd.to_datetime('21-04-2024')
    # st.write(hilton_head_sg)

    def tournament_clean_data(tournie='hilton_head', date='21-04-2024'):
        sg_approach=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/{tournie}_app.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_app'})
        ott=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/{tournie}_ott.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_ott'})
        arg=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/{tournie}_arg.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_arg'})
        putting=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/{tournie}_putting.csv').drop(['MOVEMENT','AVG'],axis=1).rename(columns={'RANK':'rank_putt'})
        total_sg=pd.merge(sg_approach,ott,how='outer')
        total_sg=pd.merge(total_sg,arg,how='outer')
        total_sg=pd.merge(total_sg,putting,how='outer')
        total_sg['Tournament']=tournie
        total_sg['Date']=pd.to_datetime(date)
        return total_sg

    def ytd_tournament_clean_data(tournie='hilton_head', date='21-04-2024'):
        sg_approach=pd.read_csv(f'C:/Users/Darragh/Documents/Python/golf/ytd_{tournie}_app.csv').drop(['MOVEMENT','AVG','RANK'],axis=1)
        ott=pd.read_csv(f'C:/Users/Darragh/Documents/Python/golf/ytd_{tournie}_ott.csv').drop(['MOVEMENT','AVG','RANK'],axis=1)
        arg=pd.read_csv(f'C:/Users/Darragh/Documents/Python/golf/ytd_{tournie}_arg.csv').drop(['MOVEMENT','AVG','RANK'],axis=1)
        putting=pd.read_csv(f'C:/Users/Darragh/Documents/Python/golf/ytd_{tournie}_putting.csv').drop(['MOVEMENT','AVG','RANK'],axis=1)
        total_sg=pd.merge(sg_approach,ott,how='outer')
        total_sg=pd.merge(total_sg,arg,how='outer')
        total_sg=pd.merge(total_sg,putting,how='outer')
        total_sg['Tournament']=tournie
        total_sg['Date']=pd.to_datetime(date)
        return total_sg

    ytd_hilton=ytd_tournament_clean_data(tournie='hilton_head', date='21-04-2024')
    # st.write(ytd_hilton)
    ytd_san_antonio=ytd_tournament_clean_data(tournie='san_antonio', date='07-04-2024')
    ytd_houston=ytd_tournament_clean_data(tournie='houston', date='31-03-2024')
    ytd_tampa_bay=ytd_tournament_clean_data(tournie='tampa_bay', date='24-03-2024')
    ytd_sawgrass=ytd_tournament_clean_data(tournie='sawgrass', date='17-03-2024')
    ytd_api=ytd_tournament_clean_data(tournie='api', date='10-03-2024')
    ytd_pga_national=ytd_tournament_clean_data(tournie='pga_national', date='03-03-2024')
    ytd_mexico=ytd_tournament_clean_data(tournie='mexico', date='25-02-2024')
    ytd_riviera=ytd_tournament_clean_data(tournie='riviera', date='18-02-2024')
    ytd_phoenix=ytd_tournament_clean_data(tournie='phoenix', date='11-02-2024')
    ytd_pebble_beach=ytd_tournament_clean_data(tournie='pebble_beach', date='04-02-2024')
    ytd_torrey_pines=ytd_tournament_clean_data(tournie='torrey_pines', date='27-01-2024')
    ytd_hawaii=ytd_tournament_clean_data(tournie='hawaii', date='14-01-2024')
    ytd_kapalua=ytd_tournament_clean_data(tournie='kapalua', date='07-01-2024')

    total_sg=pd.concat([ytd_hilton,ytd_san_antonio,ytd_houston,ytd_tampa_bay,ytd_sawgrass,ytd_api,ytd_pga_national,ytd_mexico,ytd_riviera,
                        ytd_phoenix,ytd_pebble_beach,ytd_torrey_pines,ytd_hawaii,ytd_kapalua])
    # total_sg['app_tournament']=total_sg.groupby(['PLAYER','Tournament'])['TOTAL SG:APP'].diff()
    total_sg['app_tournament']=total_sg.groupby(['PLAYER','Tournament'])['TOTAL SG:APP'].transform(lambda x: x.diff())
    st.write(total_sg)
    st.write('problem is the csv download for PGA Tour doesnt work properly')

with st.expander('Median Round Score'):
    # with st.expander('Golf Rankings'):
    cols=['R1','R2','R3','R4']
    combined_data[cols]=combined_data[cols].replace(0,np.NaN)


    # below is my manual attempt and have also the chat gpt attempt which is less code
    # st.write(combined_data[combined_data['Name'].isin({'Jordan Spieth','Scottie Scheffler'})])
    # player_1=combined_data[combined_data['Name'].isin({'Scottie Scheffler'})].loc[:,['Name','R1','R2','R3','R4','date']].set_index('date')
    # player_2=combined_data[combined_data['Name'].isin({'Jordan Spieth'})].loc[:,['Name','R1','R2','R3','R4','date']].set_index('date').add_suffix('_2')
    # both_players=pd.merge(player_1,player_2,how='outer',left_index=True,right_index=True)
    # both_players['R1_diff']=both_players['R1']-both_players['R1_2']
    # both_players['R2_diff']=both_players['R2']-both_players['R2_2']
    # both_players['R3_diff']=both_players['R3']-both_players['R3_2']
    # both_players['R4_diff']=both_players['R4']-both_players['R4_2']
    # data_raw=both_players.loc[:,['R1_diff','R2_diff','R3_diff','R4_diff']]
    # clean_data=data_raw.reset_index().melt(id_vars=['date'],var_name='round',value_name='score_diff').dropna().sort_values(by=['date','round'],ascending=[True,True])
    # st.write('median full round difference',clean_data['score_diff'].median())
    # st.write('for a 4 round tournament multiply by 4',clean_data['score_diff'].median()*4)
    # # st.write('median last 8 rounds',clean_data['score_diff'].tail(8).median())
    # st.write(data_raw.reset_index().melt(id_vars=['date'],var_name='round',value_name='score_diff').dropna())


    # df=pd.DataFrame({'Name':['Jordan','Scottie','Jordan','Scottie','Jordan'],'R1':[68,69,70,66,79],'R2':[70,65,67,72,74],'R3':[0,63,69,71,0],'R4':[0,68,72,68,0],
    #                  'date':['05-05-24','04-21-24','04-21-24','04-14-24','04-14-24']})
    # Pivot the table so that names are columns and R-values are rows per date
    df=combined_data.loc[:,['date','Name','R1', 'R2', 'R3', 'R4']]
    df_1=combined_data.loc[:,['Event Name','Name','R1', 'R2', 'R3', 'R4']]
    # st.write('comb', combined_data)
    def compute_round_median_score(df=df,first_golfer_name='Scottie Scheffler', second_golfer_name='Jordan Spieth'):
        pivot_df = df.pivot_table(index='date', columns='Name', values=['R1', 'R2', 'R3', 'R4'])
        diff_df = pivot_df.xs(first_golfer_name, axis=1, level='Name') - pivot_df.xs(second_golfer_name, axis=1, level='Name')
        diff_df.columns = [f'{col}_diff' for col in diff_df.columns]
        clean_data=diff_df.reset_index().melt(id_vars=['date'],var_name='round',value_name='score_diff').dropna().sort_values(by=['date','round'],ascending=[True,True])
        return clean_data['score_diff'].median()

    def snapshot_compute_round_median_score(df=df,first_golfer_name='Scottie Scheffler', second_golfer_name='Jordan Spieth'):
        pivot_df = df.pivot_table(index='Event Name', columns='Name', values=['R1', 'R2', 'R3', 'R4'])
        diff_df = pivot_df.xs(first_golfer_name, axis=1, level='Name') - pivot_df.xs(second_golfer_name, axis=1, level='Name')
        diff_df.columns = [f'{col}_diff' for col in diff_df.columns]
        # clean_data=diff_df.reset_index().melt(id_vars=['Event Name'],var_name='round',value_name='score_diff').dropna()
        return diff_df

    st.write('median full round difference',compute_round_median_score(df,first_golfer_name='Scottie Scheffler', second_golfer_name='Jordan Spieth'))
    # st.write('hilton head', hilton_head_results_betting)
    full_names=df_1['Name'].unique()

    # first_player=full_names.to_list()
    first_player=list(set(df_1['Name'].to_list()))    
    # st.write(len(first_player))
    # st.write(len(set(first_player)))
    # st.write('first', first_player[0])
    # st.write('first player', first_player['Name'].to_list()[0])
    # st.write('first player', first_player)
    st.write('median full round difference',compute_round_median_score(df,first_golfer_name=first_player[0], second_golfer_name='Jordan Spieth'))
    # st.write(len(first_player))
    # for x in range(1,len(first_player)):
    #     st.write(compute_round_median_score(df,first_golfer_name=first_player[0], second_golfer_name=first_player[x]))

    result=[]
    result_1=[]
    for x,i in enumerate(first_player[1:],start=1):
        result.append(i)
        result_1.append(compute_round_median_score(df,first_golfer_name=first_player[0], second_golfer_name=first_player[x]))
        # st.write(i,compute_round_median_score(df,first_golfer_name=first_player[0], second_golfer_name=first_player[x]))
    # st.write(result)
    # st.write(result_1)
    update_1 = pd.DataFrame(result)
    update_2 = pd.DataFrame(result_1)
    # update_1 = pd.concat([result])
    # update_2 = pd.concat([result_1])
    # st.write(update_1)
    # st.write(update_2)
    update_3=pd.concat([update_1,update_2],axis=1)
    update_3.columns=['Name','median']
    st.write(update_3)
    # st.write('Scheffler Spieth',snapshot_compute_round_median_score(df=df_1,first_golfer_name='Scottie Scheffler', second_golfer_name='Jordan Spieth'))

    # st.write('Scheffler Cantlay',snapshot_compute_round_median_score(df=df_1,first_golfer_name='Scottie Scheffler', second_golfer_name='Patrick Cantlay'))
    # st.write('Scheffler Clark',snapshot_compute_round_median_score(df=df_1,first_golfer_name='Scottie Scheffler', second_golfer_name='Wyndham Clark'))
    st.write('Scheffler Morikawa',snapshot_compute_round_median_score(df=df_1,first_golfer_name='Scottie Scheffler', second_golfer_name='Collin Morikawa'))
    st.write('Scheffler Burns',snapshot_compute_round_median_score(df=df_1,first_golfer_name='Scottie Scheffler', second_golfer_name='Sam Burns'))
    # st.write('it really does work....',diff_df)
    # for x,i in enumerate(first_player[1:]):
    #     st.write(x,i)