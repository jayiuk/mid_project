import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

def new_data(G, ERA, W, NP, IP, TBF, QS, WAR, RA_9, career_year, WHIP, BB,current_salary):
    pd.DataFrame([{'ERA' : ERA, 'W' : W, 'QS' : QS, 'WAR' : WAR, 'WHIP' : WHIP, 'NP/IP' : NP/IP, }])