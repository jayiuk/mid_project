import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import xgboost as xgb

def new_data(G, ERA, W, NP, IP, TBF, QS, WAR, R, career_year, WHIP, BB,current_salary, SO):
    input = pd.DataFrame([{'ERA' : ERA, 'QS_G' : QS/G, 'SO' : SO, 'WAR_x' : WAR, 'W' : W, 'IP' : IP, 'K_BB' : SO/BB, 'exp_QS' : (QS/G) * QS, 'SO_G' : SO/G, 'QS' : QS,'NP' : NP, 'RA_9' : (R/IP) * 9, '연차' : career_year, 'TBF' : TBF, '현재연봉' : current_salary, 'WHIP' : WHIP, 'K-BB' : ((SO/TBF) * 100) - ((BB/TBF) * 100) ,'NP/IP' : NP/IP}])
    with open('pitcher_salary_predict.model', 'rb') as f:
        model = pkl.load(f)
    input_d = xgb.DMatrix(input)
    prediction = model.predict(input_d)
    return prediction

def main():
    st.title('KBO 데이터 기반 야구선수 연봉 구간 예측')
    G = st.number_input('경기 수', min_value = 0)
    ERA = st.number_input('ERA', min_value = 0.0)
    W = st.number_input('승', min_value = 0)
    NP = st.number_input('투구 수', min_value = 0)
    IP = st.number_input('이닝 수', min_value = 0.0)
    TBF = st.number_input('상대한 타자 수', min_value = 0)
    QS = st.number_input('QS', min_value = 0)
    WAR = st.number_input('WAR', min_value = 0.0)
    RA_9 = st.number_input('실점', min_value = 0)
    career_year = st.number_input('연차', min_value = 1)
    WHIP = st.number_input('WHIP', min_value = 0.0)
    BB = st.number_input('볼넷', min_value = 0)
    current_salary = st.number_input('현재 연봉', min_value = 3000)
    SO = st.number_input('삼진', min_value = 0)


    if st.button('예측 시작'):
        r = new_data(G, ERA, W, NP, IP, TBF, QS, WAR, RA_9, career_year, WHIP, BB, current_salary, SO)
        if r == 0:
            result = 'D'
        elif r == 1:
            result = 'C'
        elif r == 2:
            result = 'B'
        else:
            result = 'A'
        
        st.success(f'연봉 구간 : {result}')


if __name__ == "__main__":
    main()
