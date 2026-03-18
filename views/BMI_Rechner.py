import pandas as pd
import streamlit as st
from utils.data_manager import DataManager

from functions.BMI_Rechner import bmi_rechner, bmi_kategorie

st.title("BMI Rechner")

with st.form("BMI_form"):
    gewicht = st.number_input("Geben Sie Ihr Gewicht in kg ein:")
    groesse = st.number_input("Geben Sie Ihre Körpergröße in m ein:")

    button = st.form_submit_button("Berechnen")

if button:
    result = bmi_rechner(gewicht, groesse)
    st.write(f"Ihr BMI ist: {result['bmi']}")
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f"Kategorie: {result['bmi_kategorie ']}")
    st.balloons()
    
    st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])])

 # --- CODE UPDATE: save data to data manager ---
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---

st.dataframe(st.session_state['data_df'])

