import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Cross check against SG Average total here
# https://www.pgatour.com/stats/stat.02675.html

# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02674.html')[1]).drop(['RANK LAST WEEK'], axis=1))
# b=pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02564.html')[1]).drop(['RANK LAST WEEK'], axis=1)
# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02674.y2021.html')[1]).drop(['RANK LAST WEEK'], axis=1))
# b=pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.02564.y2021.html')[1]).drop(['RANK LAST WEEK'], axis=1)
# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.144.y2021.html')[1]).drop(['RANK LAST WEEK'], axis=1))
# b=pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.144.html')[1]).drop(['RANK LAST WEEK'], axis=1)
# a=(pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.144.html')[1]).drop(['RANK LAST WEEK'], axis=1))
# b=pd.DataFrame(pd.read_html('https://www.pgatour.com/stats/stat.144.html')[1]).drop(['RANK LAST WEEK'], axis=1)

# st.write(a)
# st.write(b)

# df=pd.concat([a,b])
# df.to_csv('C:/Users/Darragh/Documents/Python/golf/par_5_total.csv')
par_5=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/par_5_total.csv').drop(['Unnamed: 0'],axis=1)
par_5_group=par_5.groupby('PLAYER NAME').sum().reset_index()
par_5_group['par_5_avg']=par_5_group['TOTAL STROKES'] / par_5_group['TOTAL HOLES']
par_5_group['par_5_sg']=(5-par_5_group['par_5_avg'])*4
par_5_group['par_5_rank']=(par_5_group['par_5_avg']).rank(method='dense', ascending=True).astype(int)
par_5_group=par_5_group.set_index('PLAYER NAME')
st.write(par_5_group)



def run(x):
    df=pd.merge(a, b, on=['PLAYER NAME', 'ROUNDS', 'MEASURED ROUNDS'])    
    df=df.drop(df.columns[[0,8,3,9]], axis=1)
    df['SG:OTT']=df['SG:OTT']*df['MEASURED ROUNDS']
    df['SG:APR']=df['SG:APR']*df['MEASURED ROUNDS']
    df['SG:ARG']=df['SG:ARG']*df['MEASURED ROUNDS']
    col_list=['SG:OTT','SG:APR','SG:ARG','TOTAL SG:PUTTING']
    df['SG: TOTAL']=df[col_list].sum(axis=1)
    cols_to_move = ['PLAYER NAME','MEASURED ROUNDS','ROUNDS','SG:OTT','SG:APR','SG:ARG','TOTAL SG:PUTTING',
    'SG: TOTAL']
    cols = cols_to_move + [col for col in df if col not in cols_to_move]
    df=df[cols]
    df['year']=2022
    df.to_csv('C:/Users/Darragh/Documents/Python/golf/rankings_2022.csv')
    return df

df_2021=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/rankings_2021.csv')
df_2022=pd.read_csv('C:/Users/Darragh/Documents/Python/golf/rankings_2022.csv')
df=pd.concat([df_2021,df_2022]).drop(['Unnamed: 0','ROUNDS','year'],axis=1).rename(columns={'SG:OTT':'TOTAL SG:OTT','SG:APR':'TOTAL SG:APR','SG:ARG':'TOTAL SG:ARG'})
df_group=df.groupby('PLAYER NAME').sum().reset_index()
# st.write(df_group)

def clean_golf_tee(df):
    df['SG:OTT']=df['TOTAL SG:OTT']/df['MEASURED ROUNDS']
    df['SG:APR']=df['TOTAL SG:APR']/df['MEASURED ROUNDS']
    df['SG:ARG']=df['TOTAL SG:ARG']/df['MEASURED ROUNDS']
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

    
    # df['ROUNDS']=df['ROUNDS'].astype(int)
    df['MEASURED ROUNDS']=df['MEASURED ROUNDS'].astype(int)
    df['SG_Rank']=df['SG_Rank'].astype(int)
    df['Appr_Rank']=df['Appr_Rank'].astype(int)
    df['ARG_Rank']=df['ARG_Rank'].astype(int)
    df['Putt_Rank']=df['PUTT_Rank'].astype(int)
    df['Tee_Rank']=df['Tee_Rank'].astype(int)
    df['Tee_ARG_Rank']=df['Tee_ARG_Rank'].astype(int)
    df['Tee_App_Rank']=df['Tee_App_Rank'].astype(int)
    df['Rev_Rank_Var']=df['Rev_Rank_Var'].astype(int)
    # df['Rank_Equal']=df['Rank_Equal'].astype(int)
    # df=df.reset_index()
    cols_to_move = ['PLAYER NAME','MEASURED ROUNDS','SG_Rank','Tee_Rank','Appr_Rank','Tee_App_Rank','ARG_Rank','Putt_Rank']
    cols = cols_to_move + [col for col in df if col not in cols_to_move]
    df=df[cols]
    df=df.reset_index().set_index('PLAYER NAME').drop(['index'],axis=1)
    return df.sort_values(by='SG_Rank', ascending=True)

df=clean_golf_tee(df_group)
st.write(df)

merged=pd.concat([df, par_5_group],axis=1)
merged['par_5_tee_app']=merged['par_5_sg']+merged['SG: Tee_App_AVG']
merged['par_5_tee_app_rank']=merged['par_5_tee_app'].rank(method='dense', ascending=False).astype(int)
df=merged.copy()
cols_to_move = ['MEASURED ROUNDS','par_5_tee_app_rank','Tee_App_Rank','par_5_rank','SG_Rank','Tee_Rank','Appr_Rank','ARG_Rank','Putt_Rank']
cols = cols_to_move + [col for col in df if col not in cols_to_move]
df=df[cols]


st.write(df)