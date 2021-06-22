# -*- coding: utf-8 -*-
######################
# Import libraries
######################
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import xgboost as xgb

from sklearn.ensemble import RandomForestClassifier



st.image('./titleApp4.png')

# Patient Input Parameters
st.sidebar.header('Patient Input Parameters')

def user_input_features():
    Gender = st.sidebar.radio('Gender',['Female','Male'])
    Albumin = st.sidebar.slider('Albumin',0, 500, 38)
    Glucose_Fasting = st.sidebar.slider('Fasting Glucose',40, 300, 97)
    Urea_BUN = st.sidebar.slider('Urea (BUN)',1, 76, 12)
    Cholesterol = st.sidebar.slider('Cholesterol',72,450, 188)
    Protein_total = st.sidebar.slider('Total Protein',5.0, 10.0,7.5)
    Sodium = st.sidebar.slider('Sodium', 100, 147, 138)
    Creatinine = st.sidebar.slider('Creatinine',0.2, 7.3, 0.74)
    Hemoglobin = st.sidebar.slider('Hemoglobin',6, 20, 14)
    Bilirubin_total = st.sidebar.slider('Total Bilirubin', 0.1, 4.4, 0.6)
    Triglycerides = st.sidebar.slider('Triglycerides', 16, 400, 109)
    HDL = st.sidebar.slider('HDL', 8, 160, 52)
    LDL = st.sidebar.slider('LDL', 25, 320, 112)
    Calcium = st.sidebar.slider('Calcium', 7, 12, 9)
    Potassium = st.sidebar.slider('Potassium',2.5, 5.6, 4.0)
    Hematocrit = st.sidebar.slider('Hematocrit', 21, 58, 41)
    MCHC = st.sidebar.slider('MCHC', 25, 38, 33)
    MCV = st.sidebar.slider('MCV', 56, 120, 89)
    Platelets = st.sidebar.slider('Platelets', 10, 500, 272)
    Protoporphyrin = st.sidebar.slider('Protoporphyrin', 0, 200,55)

    if Gender == 'Female':
        female = 1
        male = 0
    else:
        female = 0
        male = 1

    data = {'female':female,'male': male,
            'URXUMA':Albumin,'LBXGLU':Glucose_Fasting,
            'LBXSBU':Urea_BUN,'LBXTC':Cholesterol,
            'LBXSTP':Protein_total,'LBXSNASI':Sodium,
            'LBXSCR':Creatinine,'LBXHGB':Hemoglobin,
            'LBXSTB':Bilirubin_total,'LBXSTR':Triglycerides,
            'LBDHDL':HDL,'LBDLDL':LDL,
            'LBXSCA':Calcium,'LBXSKSI':Potassium,
            'LBXHCT':Hematocrit,'LBXMC':MCHC,
            'LBXMCVSI':MCV,'LBXPLTSI':Platelets,'LBXEPP':Protoporphyrin}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()



# Reads in saved model
load_model = pickle.load(open('xgb_nhanes_bldage_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_model.predict(df)
#prediction_proba = load_model.predict_proba(df)
aging_rate = 'Coming soon!'

st.write("""
           **Oxcitas blood age prototype 23.06.2021**
           """)
#st.subheader('Sepsis:')
#st.write("""
            #Sepsis is a life-threatening condition caused by your body’s response to an infection (bacterial, viral or fungal) and damages its own tissues.

            #Sepsis is the leading cause of global mortality, around 20% of annual global death. Eraly detection is vital in the survival of the patient. Every 10min, death risk increases by 1%.
            #""")
st.subheader('Input:')
st.write(df)
st.subheader('Predicted Blood Age:')
st.write(prediction)
st.subheader('Blood aging rate:')
st.write(aging_rate)
